// Fill out your copyright notice in the Description page of Project Settings.

#include "TCPConnectionPlugin.h"
#include "TCPListenComponent.h"


// Sets default values for this component's properties
UTCPListenComponent::UTCPListenComponent()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = true;

	m_SocketName = "SocketListener";
	FIPv4Address::Parse("0.0.0.0", m_IPAddress);
	m_Port = 50505;

	// default buffer
	m_BufferSize = 1024;
}

// Delete components properties
UTCPListenComponent::~UTCPListenComponent()
{
	closeSockets();
}


// Called when the game starts
void UTCPListenComponent::BeginPlay()
{
	Super::BeginPlay();

	StartupNetworking();
	
}


// Called every frame
void UTCPListenComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

	// ...
}

void UTCPListenComponent::StartupNetworking()
{
	if (StartTCPReceiver())
	{
		UE_LOG(LogTemp, Warning, TEXT("TCP Socket Listener started"));
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("TCP Socket Listener failed"));
	}
}

bool UTCPListenComponent::StartTCPReceiver()
{
	// CreateTCPConnectionListener
	ListenerSocket = CreateTCPConnectionListener(m_SocketName, m_IPAddress, m_Port, m_BufferSize);

	//Not created?
	if (!ListenerSocket)
	{
		UE_LOG(LogTemp, Warning, TEXT("Listener socket failed to start"));
		return false;
	}

	// Start Listener
	// Listens until a connection is received
	// Then creates a socket for the connection
	FTimerDelegate TimerDel;
	TimerDel.BindUFunction(this, FName("TCPConnectionListener"));

	GetWorld()->GetTimerManager().SetTimer(TimerHandle,
		TimerDel, 0.01, true);
	return true;
}

FSocket * UTCPListenComponent::CreateTCPConnectionListener(const FString & SocketName, const FIPv4Address IPAddress, const int32 Port, const int32 ReceiveBufferSize)
{
	// Create endpoint
	FIPv4Endpoint Endpoint(FIPv4Address(
		IPAddress.A, IPAddress.B,
		IPAddress.C, IPAddress.D),
		Port);

	// Create Socket and tell it to listen for connections
	FSocket* ListenSocket = FTcpSocketBuilder(*SocketName)
		.AsReusable()
		.BoundToEndpoint(Endpoint)
		.Listening(8);

	// if socket failed to be created
	if (!ListenSocket)
	{
		return NULL;
	}

	// Set Buffer Size
	int32 NewSize = 0;
	ListenSocket->SetReceiveBufferSize(ReceiveBufferSize, NewSize);

	return ListenSocket;
}

void UTCPListenComponent::TCPConnectionListener()
{
	if (!ListenerSocket)
	{
		return;
	}

	// Remote address
	TSharedRef<FInternetAddr> RemoteAddress = ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM)->CreateInternetAddr();
	bool Pending;

	// handle incoming connections
	if (ListenerSocket->HasPendingConnection(Pending))
	{
		// Destroy the current connection if new one pending
		if (ConnectionSocket)
		{
			ConnectionSocket->Close();
			ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM)->DestroySocket(ConnectionSocket);
		}

		// New Connection received
		ConnectionSocket = ListenerSocket->Accept(*RemoteAddress, TEXT("TCP Received Socket Connection"));

		// if new connection connected
		if (ConnectionSocket != NULL)
		{
			// Global cache of current Remote Address
			RemoteAddressForConnection = FIPv4Endpoint(RemoteAddress);

			UE_LOG(LogTemp, Warning, TEXT("Accepted Connection!"));

			// start timer function
			FTimerDelegate TimerDel;
			TimerDel.BindUFunction(this, FName("TCPSocketListener"));

			GetWorld()->GetTimerManager().SetTimer(TimerHandle,
				TimerDel, 0.01, true);
		}
	}
}

void UTCPListenComponent::TCPSocketListener()
{
	if (!ConnectionSocket)
	{
		return;
	}

	// Binary Array
	TArray<uint8> ReceivedData;
	uint32 Size;

	// amount of data read
	int32 DataRead = 0;

	// go through the data until it's all been read
	while (ConnectionSocket->HasPendingData(Size))
	{
		// fill array
		ReceivedData.Init(FMath::Min(Size, 65507u), m_BufferSize);

		// get data and store into binary array
		ConnectionSocket->Recv(ReceivedData.GetData(), m_BufferSize, DataRead);
	}

	// if there's nothing in our array
	if (DataRead <= 0)
	{
		return;
	}

	UE_LOG(LogTemp, Warning, TEXT("Data Received!"));

	// convert binary array
	ReceivedDataArray.Add(BinaryArrayToInt(ReceivedData, m_BufferSize));

	// output binary array 
	UE_LOG(LogTemp, Warning, TEXT("Data: %d"), ReceivedDataArray[0][0]);
}

void UTCPListenComponent::closeSockets()
{
	if (ConnectionSocket)
	{
		ConnectionSocket->Close();
		ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM)->
			DestroySocket(ConnectionSocket);
	}
	if (ListenerSocket)
	{
		ListenerSocket->Close();
		ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM)->
			DestroySocket(ListenerSocket);
	}
}

std::string UTCPListenComponent::BinaryArrayToString(TArray<uint8>& ReceivedData)
{
	// This function was written when python script was used for testing
	// | was used to break loop

	std::string ReceivedString;

	for (int i = 0; i <= 50; i++)
	{
		// break loop if character is a | (ASCII code is 124)
		if (static_cast<char>(ReceivedData[i]) == 124)
		{
			break;
		}
		// static cast a ASCII decimal to a char	
		else
		{
			ReceivedString += static_cast<char>(ReceivedData[i]);
		}
	}
	return ReceivedString;
}

TArray<int> UTCPListenComponent::BinaryArrayToInt(TArray<uint8>& ReceivedData, int ArraySize)
{
	// array for holding converted bytes
	TArray<int> convertedData;
	uint32 Size = 0;
	// fill array
	convertedData.Init(FMath::Min(Size, 65507u), ArraySize);

	for (int i = 0; i < ArraySize; i++)
	{
		// cast byte to unsigned char then cast to int
		int convertedInt = static_cast<int>(static_cast<char>(ReceivedData[0]));
		convertedData[i] = convertedInt;
	}
	return convertedData;
}

FString UTCPListenComponent::getLocalIP()
{
	bool canBind = false;
	// create address and store the localhost address in it
	TSharedRef<FInternetAddr> IPAddress =
		ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM)->
		GetLocalHostAddr(*GLog, canBind);

	// return the IPAddress as a string
	return IPAddress->ToString(false);
}

TArray<int> UTCPListenComponent::ReturnReceivedIntData()
{
	//if there's data stored
	if (ReceivedDataArray.Num() > 0)
	{
		return ReceivedDataArray[0];
	}
	TArray<int32> DefaultData;
	uint32 Size = 0;
	DefaultData.Init(FMath::Min(Size, 65507u), m_BufferSize);

	// return NULL data if no new recieved data
	// just an array of 0's
	return DefaultData;
}

void UTCPListenComponent::removeFirstReceivedIntData()
{
	// if the array is not empty
	if (ReceivedDataArray.Num() > 0)
	{
		ReceivedDataArray.RemoveAt(0);
	}
}

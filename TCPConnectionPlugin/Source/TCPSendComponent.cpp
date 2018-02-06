// Fill out your copyright notice in the Description page of Project Settings.

#include "TCPConnectionPlugin.h"
#include "TCPSendComponent.h"


// Sets default values for this component's properties
UTCPSendComponent::UTCPSendComponent()
{
	// Set this component to be initialized when the game starts, and to be ticked every frame.  You can turn these features
	// off to improve performance if you don't need them.
	PrimaryComponentTick.bCanEverTick = true;

	// ...
}


// Called when the game starts
void UTCPSendComponent::BeginPlay()
{
	Super::BeginPlay();

	// ...
	
}


// Called every frame
void UTCPSendComponent::TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction)
{
	Super::TickComponent(DeltaTime, TickType, ThisTickFunction);

	// ...
}

void UTCPSendComponent::StartupNetworking()
{
	// Start up TCP/IP connection
	if (StartTCPReceiver())
	{
		UE_LOG(LogTemp, Warning, TEXT("TCP Socket Listener"));
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("TCP Socket Listener didn't launch"));
	}
}

bool UTCPSendComponent::StartTCPReceiver()
{
	// CreateTCPConnectionListener
	ListenerSocket = CreateTCPConnectionListener();

	// if the Receiver did not start
	if (!ListenerSocket)
	{
		UE_LOG(LogTemp, Warning, TEXT("Listener socket did not start"));
		return false;
	}

	// create timer function delegate
	FTimerDelegate TimerDel;
	TimerDel.BindUFunction(this, FName("TCPConnectionSender"));

	// start the timer function
	GetWorld()->GetTimerManager().SetTimer(TimerHandle,
		TimerDel, 0.01, true);
	UE_LOG(LogTemp, Warning, TEXT("Listener socket started"));
	// if the Reciever started
	return true;
}

FSocket * UTCPSendComponent::CreateTCPConnectionListener()
{
	// Create Socket Endpoint
	FIPv4Endpoint Endpoint(FIPv4Address(
		IPAddress.A, IPAddress.B,
		IPAddress.C, IPAddress.D),
		m_Port);

	// Create Socket
	FSocket* ListenSocket = FTcpSocketBuilder(*m_SocketName);

	// Set Buffer Size for socket
	int32 NewSize = 0;
	ListenSocket->SetSendBufferSize(m_BufferSize, NewSize);

	// return the socket
	return ListenSocket;
}

void UTCPSendComponent::TCPConnectionSender()
{
	// return if the socket doesn't exist
	if (!ListenerSocket)
	{
		return;
	}

	// Create the address for remote connection
	TSharedRef<FInternetAddr> m_InternetAddress = ISocketSubsystem::Get(PLATFORM_SOCKETSUBSYSTEM)->CreateInternetAddr();
	m_InternetAddress->SetIp(IPAddress.Value);
	m_InternetAddress->SetPort(m_Port);

	//bool Pending;

	// if connected
	if (ListenerSocket->Connect(*m_InternetAddress))
	{
		// if the connection socket is not empty then create sender
		if (ListenerSocket != NULL)
		{
			// Global cache of current Remote Address
			RemoteAddressForConnection = FIPv4Endpoint(m_InternetAddress);

			UE_LOG(LogTemp, Warning, TEXT("Accepted Connection!"));

			// Is this even needed anymore??
			//FTimerDelegate TimerDel;

			//TimerDel.BindUFunction(this, FName("TCPSocketSender"));

			//GetWorld()->GetTimerManager().SetTimer(TimerHandle,
			//	TimerDel, 0.01, true);
		}
	}
}

void UTCPSendComponent::TCPSocketSender()
{
	// if the connection socket doesn't exist
	if (!ListenerSocket)
	{
		return;
	}

	// Binary Array for containing data we are sending

	uint32 Size = 0;

	// The amount of data we sent
	int32 BytesSent = -1;
	//ListenerSocket->Send(m_OutputData.GetData(), m_OutputData.Num(), BytesSent);

	// if the socket didn't send any data
	if (BytesSent < 0)
	{
		return;
	}

	UE_LOG(LogTemp, Warning, TEXT("Data Sent! %d"), BytesSent);

	// clear array
	m_OutputData.Init(FMath::Min(Size, 65507u), 50);

}

void UTCPSendComponent::setIPAddress(FString newIP)
{
	IPAddressString = newIP;
	FIPv4Address::Parse(IPAddressString, IPAddress);
}

void UTCPSendComponent::sendData(uint8 label, TArray<uint8> OutputData)
{
	// if the connection socket doesn't exist
	if (!ListenerSocket)
	{
		return;
	}

	// first element is what data is in the array
	m_OutputData.EmplaceAt(0, label);

	// The amount of data we sent
	int32 BytesSent = 0;

	ListenerSocket->Send(OutputData.GetData(), OutputData.Num(), BytesSent);

	// if the socket didn't send any data
	if (BytesSent == -1)
	{
		return;
	}

	UE_LOG(LogTemp, Warning, TEXT("Data Sent! %d"), BytesSent);
}
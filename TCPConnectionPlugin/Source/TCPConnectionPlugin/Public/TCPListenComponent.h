// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "Components/ActorComponent.h"
#include "engine.h"
#include "Networking.h"
#include <string>
#include "TCPListenComponent.generated.h"


UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class TCPCONNECTIONPLUGIN_API UTCPListenComponent : public UActorComponent
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	UTCPListenComponent();
	~UTCPListenComponent();

protected:
	// Called when the game starts
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;


	// Socket
	void StartupNetworking();

	bool StartTCPReceiver();

	FSocket* CreateTCPConnectionListener(
		const FString& SocketName,
		const FIPv4Address IPAddress,
		const int32 Port,
		const int32 ReceiveBufferSize
	);

	// Timer functions
	UFUNCTION()
		void TCPConnectionListener();
	UFUNCTION()
		void TCPSocketListener();

	void closeSockets();

	// Convert Binary Array to string
	std::string BinaryArrayToString(TArray<uint8> &ReceivedData);

	// Convert Binary Array to int
	TArray<int> BinaryArrayToInt(TArray<uint8> &ReceivedData, int ArraySize);

	// Returns the computers IPAddress as string
	UFUNCTION(BlueprintCallable, Category = "Network")
		FString getLocalIP();

	// get the recieved data
	UFUNCTION(BlueprintCallable, Category = "Network")
		TArray<int> ReturnReceivedIntData();

	// delete the first array in our recieved data
	// call this function when the data is no longer needed
	UFUNCTION(BlueprintCallable, Category = "Network")
		void removeFirstReceivedIntData();

protected:

	FSocket* ListenerSocket;
	FSocket* ConnectionSocket;
	FIPv4Endpoint RemoteAddressForConnection;

	FTimerHandle TimerHandle;

	FString m_SocketName;

	// Local IPAddress
	FIPv4Address m_IPAddress;

	// Port used for connection connect
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = NetworkStats)
		int32 m_Port;

	// Size of data being sent/recieved
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = NetworkStats)
		int32 m_BufferSize;

	// the data received from the mobile app
	// currently the listener socket converts the recieved binary data to ints
	TArray<TArray<int>> ReceivedDataArray;	
};
// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "Components/ActorComponent.h"
#include "Networking.h"
#include <vector>
#include "engine.h"
#include "TCPSendComponent.generated.h"


UCLASS( ClassGroup=(Custom), meta=(BlueprintSpawnableComponent) )
class TCPCONNECTIONPLUGIN_API UTCPSendComponent : public UActorComponent
{
	GENERATED_BODY()

public:	
	// Sets default values for this component's properties
	UTCPSendComponent();

protected:
	// Called when the game starts
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void TickComponent(float DeltaTime, ELevelTick TickType, FActorComponentTickFunction* ThisTickFunction) override;
	
	UFUNCTION(BlueprintCallable, Category = "Network")
		void StartupNetworking();

	bool StartTCPReceiver();
	FSocket* CreateTCPConnectionListener();

	// timer functions
	UFUNCTION()
		void TCPConnectionSender();
	UFUNCTION()
		void TCPSocketSender();

	// set the IPAddress
	UFUNCTION(BlueprintCallable, Category = "Network")
		void setIPAddress(FString newIP);

	// label is what the data we're sending is e.g. health or position
	// output data is the data we're sending
	UFUNCTION(BlueprintCallable, Category = "Network")
		void sendData(uint8 label, TArray<uint8> OutputData);


protected:

	FSocket* ListenerSocket;		// socket for listening for a connection
	FSocket* ConnectionSocket;		// socket for connecting to other device

	FIPv4Endpoint RemoteAddressForConnection;

	FTimerHandle TimerHandle;

	FString m_SocketName;

	// IP and Port
	// IPAddress of host
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = NetworkStats)
		FString IPAddressString;
	FIPv4Address IPAddress;

	// Port used for connection
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = NetworkStats)
		int32 m_Port;

	// Size of data being sent/recieved
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = NetworkStats)
		int32 m_BufferSize;

	// array for data we're transmitting
	TArray<uint8> m_OutputData;	
};

// Fill out your copyright notice in the Description page of Project Settings.

#include "UnrealEnginePythonPrivatePCH.h"
#include "PipConsoleManager.h"

UPipConsoleManager::UPipConsoleManager(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{

}

//using windows api for now
#if PLATFORM_WINDOWS
#include "AllowWindowsPlatformTypes.h"



void UPipConsoleManager::pip(FString Arg1, FString Arg2)
{
	UE_LOG(LogTemp, Log, TEXT("you passed %s and %s"), *Arg1, *Arg2);


}

#include "HideWindowsPlatformTypes.h"

#else

void UPipConsoleManager::pip(FString Arg1, FString Arg2)
{
	UE_LOG(LogTemp, Log, TEXT("platform not supported"));
}

#endif
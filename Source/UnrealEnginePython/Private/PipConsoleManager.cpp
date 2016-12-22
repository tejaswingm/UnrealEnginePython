// Fill out your copyright notice in the Description page of Project Settings.

#include "UnrealEnginePythonPrivatePCH.h"
#include "PipConsoleManager.h"

void UPipConsoleManager::PyPip(FString Arg1, FString Arg2)
{
	UE_LOG(LogTemp, Log, TEXT("you passed %s and %s"), *Arg1, *Arg2);
}

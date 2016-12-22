// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "PipConsoleManager.generated.h"

/**
 * 
 */
UCLASS()
class UPipConsoleManager : public UCheatManager
{
	GENERATED_UCLASS_BODY()
	
	UFUNCTION(Exec)
	void PyPip(FString Arg1, FString Arg2);
	
};

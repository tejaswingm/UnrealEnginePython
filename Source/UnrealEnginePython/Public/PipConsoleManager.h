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
	
	/* Command to execute pip from ue4 console*/
	UFUNCTION(Exec)
	void pip(FString Arg1, FString Arg2);
	
};

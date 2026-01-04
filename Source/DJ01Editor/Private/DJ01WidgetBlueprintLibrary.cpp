// Copyright Epic Games, Inc. All Rights Reserved.

#include "DJ01WidgetBlueprintLibrary.h"
#include "WidgetBlueprint.h"
#include "Blueprint/WidgetTree.h"
#include "Components/Widget.h"
#include "Components/PanelWidget.h"
#include "Components/CanvasPanel.h"
#include "Components/CanvasPanelSlot.h"
#include "Components/ProgressBar.h"
#include "Components/TextBlock.h"
#include "Components/Image.h"
#include "UObject/Package.h"
#include "UObject/SavePackage.h"
#include "Dom/JsonObject.h"
#include "Serialization/JsonReader.h"
#include "Serialization/JsonSerializer.h"

// ===== 基础操作 =====

UWidgetTree* UDJ01WidgetBlueprintLibrary::GetWidgetTree(UWidgetBlueprint* WidgetBlueprint)
{
	if (!WidgetBlueprint)
	{
		UE_LOG(LogTemp, Warning, TEXT("GetWidgetTree: WidgetBlueprint is null"));
		return nullptr;
	}
	
	return WidgetBlueprint->WidgetTree;
}

UWidget* UDJ01WidgetBlueprintLibrary::GetRootWidget(UWidgetBlueprint* WidgetBlueprint)
{
	if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree)
	{
		return nullptr;
	}
	
	return WidgetBlueprint->WidgetTree->RootWidget;
}

bool UDJ01WidgetBlueprintLibrary::SetRootWidget(UWidgetBlueprint* WidgetBlueprint, UWidget* RootWidget)
{
	if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree)
	{
		UE_LOG(LogTemp, Warning, TEXT("SetRootWidget: Invalid WidgetBlueprint or WidgetTree"));
		return false;
	}
	
	WidgetBlueprint->Modify();
	WidgetBlueprint->WidgetTree->RootWidget = RootWidget;
	
	UE_LOG(LogTemp, Log, TEXT("SetRootWidget: Set root widget to %s"), RootWidget ? *RootWidget->GetName() : TEXT("null"));
	return true;
}

// ===== 控件创建 =====

UWidget* UDJ01WidgetBlueprintLibrary::CreateWidget(UWidgetBlueprint* WidgetBlueprint, TSubclassOf<UWidget> WidgetClass, FName WidgetName)
{
	if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree || !WidgetClass)
	{
		UE_LOG(LogTemp, Warning, TEXT("CreateWidget: Invalid parameters"));
		return nullptr;
	}
	
	WidgetBlueprint->Modify();
	
	UWidget* NewWidget = WidgetBlueprint->WidgetTree->ConstructWidget<UWidget>(WidgetClass, WidgetName);
	if (NewWidget)
	{
		UE_LOG(LogTemp, Log, TEXT("CreateWidget: Created widget %s of type %s"), *WidgetName.ToString(), *WidgetClass->GetName());
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("CreateWidget: Failed to create widget %s"), *WidgetName.ToString());
	}
	
	return NewWidget;
}

UWidget* UDJ01WidgetBlueprintLibrary::CreateCanvasPanel(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
	return CreateWidget(WidgetBlueprint, UCanvasPanel::StaticClass(), WidgetName);
}

UWidget* UDJ01WidgetBlueprintLibrary::CreateProgressBar(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
	return CreateWidget(WidgetBlueprint, UProgressBar::StaticClass(), WidgetName);
}

UWidget* UDJ01WidgetBlueprintLibrary::CreateTextBlock(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
	return CreateWidget(WidgetBlueprint, UTextBlock::StaticClass(), WidgetName);
}

UWidget* UDJ01WidgetBlueprintLibrary::CreateImage(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
	return CreateWidget(WidgetBlueprint, UImage::StaticClass(), WidgetName);
}

// ===== 层级操作 =====

bool UDJ01WidgetBlueprintLibrary::AddChildToPanel(UWidget* Parent, UWidget* Child)
{
	if (!Parent || !Child)
	{
		UE_LOG(LogTemp, Warning, TEXT("AddChildToPanel: Invalid parameters"));
		return false;
	}
	
	UPanelWidget* PanelWidget = Cast<UPanelWidget>(Parent);
	if (!PanelWidget)
	{
		UE_LOG(LogTemp, Warning, TEXT("AddChildToPanel: Parent is not a PanelWidget"));
		return false;
	}
	
	UPanelSlot* Slot = PanelWidget->AddChild(Child);
	if (Slot)
	{
		UE_LOG(LogTemp, Log, TEXT("AddChildToPanel: Added %s to %s"), *Child->GetName(), *Parent->GetName());
		return true;
	}
	
	return false;
}

bool UDJ01WidgetBlueprintLibrary::AddChildToCanvas(UWidget* CanvasPanelWidget, UWidget* Child, FVector2D Position, FVector2D Size)
{
	if (!CanvasPanelWidget || !Child)
	{
		UE_LOG(LogTemp, Warning, TEXT("AddChildToCanvas: Invalid parameters"));
		return false;
	}
	
	UCanvasPanel* CanvasPanel = Cast<UCanvasPanel>(CanvasPanelWidget);
	if (!CanvasPanel)
	{
		UE_LOG(LogTemp, Warning, TEXT("AddChildToCanvas: Widget is not a CanvasPanel"));
		return false;
	}
	
	UCanvasPanelSlot* Slot = Cast<UCanvasPanelSlot>(CanvasPanel->AddChild(Child));
	if (Slot)
	{
		// 设置位置和大小
		Slot->SetPosition(Position);
		Slot->SetSize(Size);
		
		// 设置默认锚点为左上角
		Slot->SetAnchors(FAnchors(0.0f, 0.0f, 0.0f, 0.0f));
		
		UE_LOG(LogTemp, Log, TEXT("AddChildToCanvas: Added %s to CanvasPanel at (%.1f, %.1f) size (%.1f, %.1f)"), 
			*Child->GetName(), Position.X, Position.Y, Size.X, Size.Y);
		return true;
	}
	
	return false;
}

// ===== 查找操作 =====

UWidget* UDJ01WidgetBlueprintLibrary::FindWidgetByName(UWidgetBlueprint* WidgetBlueprint, FName WidgetName)
{
	if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree)
	{
		return nullptr;
	}
	
	return WidgetBlueprint->WidgetTree->FindWidget(WidgetName);
}

TArray<UWidget*> UDJ01WidgetBlueprintLibrary::GetAllWidgets(UWidgetBlueprint* WidgetBlueprint)
{
	TArray<UWidget*> AllWidgets;
	
	if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree)
	{
		return AllWidgets;
	}
	
	WidgetBlueprint->WidgetTree->GetAllWidgets(AllWidgets);
	return AllWidgets;
}

// ===== 保存操作 =====

void UDJ01WidgetBlueprintLibrary::MarkDirty(UWidgetBlueprint* WidgetBlueprint)
{
	if (WidgetBlueprint)
	{
		WidgetBlueprint->Modify();
	}
}

bool UDJ01WidgetBlueprintLibrary::SaveWidgetBlueprint(UWidgetBlueprint* WidgetBlueprint)
{
	if (!WidgetBlueprint)
	{
		return false;
	}
	
	// 获取 Package
	UPackage* Package = WidgetBlueprint->GetOutermost();
	if (!Package)
	{
		UE_LOG(LogTemp, Warning, TEXT("SaveWidgetBlueprint: Failed to get package"));
		return false;
	}
	
	// 标记为脏
	Package->MarkPackageDirty();
	
	// 获取文件路径
	FString PackageFileName = FPackageName::LongPackageNameToFilename(
		Package->GetName(), 
		FPackageName::GetAssetPackageExtension()
	);
	
	// 使用旧版 API 保存
	bool bSaved = UPackage::SavePackage(
		Package, 
		WidgetBlueprint, 
		RF_Standalone,           // EObjectFlags
		*PackageFileName,        // Filename
		GError,                  // Error output
		nullptr,                 // Linker
		false,                   // bForceByteSwapping
		true,                    // bWarnOfLongFilename
		SAVE_None                // SaveFlags
	);
	
	if (bSaved)
	{
		UE_LOG(LogTemp, Log, TEXT("SaveWidgetBlueprint: Saved %s"), *PackageFileName);
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("SaveWidgetBlueprint: Failed to save %s"), *PackageFileName);
	}
	
	return bSaved;
}

// ===== 批量操作 =====

bool UDJ01WidgetBlueprintLibrary::CreateWidgetsFromJson(UWidgetBlueprint* WidgetBlueprint, const FString& SchemaJson)
{
	if (!WidgetBlueprint || !WidgetBlueprint->WidgetTree)
	{
		UE_LOG(LogTemp, Warning, TEXT("CreateWidgetsFromJson: Invalid WidgetBlueprint"));
		return false;
	}
	
	// 解析 JSON
	TSharedPtr<FJsonObject> JsonObject;
	TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(SchemaJson);
	
	if (!FJsonSerializer::Deserialize(Reader, JsonObject) || !JsonObject.IsValid())
	{
		UE_LOG(LogTemp, Warning, TEXT("CreateWidgetsFromJson: Failed to parse JSON"));
		return false;
	}
	
	// 获取组件数组
	const TArray<TSharedPtr<FJsonValue>>* ComponentsArray;
	if (!JsonObject->TryGetArrayField(TEXT("components"), ComponentsArray))
	{
		UE_LOG(LogTemp, Warning, TEXT("CreateWidgetsFromJson: No 'components' array in JSON"));
		return false;
	}
	
	WidgetBlueprint->Modify();
	
	// 递归创建控件的 Lambda
	TFunction<UWidget*(const TSharedPtr<FJsonObject>&, UWidget*)> CreateWidgetRecursive;
	CreateWidgetRecursive = [&](const TSharedPtr<FJsonObject>& CompDef, UWidget* Parent) -> UWidget*
	{
		FString Name = CompDef->GetStringField(TEXT("name"));
		FString Type = CompDef->GetStringField(TEXT("type"));
		
		// 类型映射
		TSubclassOf<UWidget> WidgetClass = nullptr;
		if (Type == TEXT("CanvasPanel")) WidgetClass = UCanvasPanel::StaticClass();
		else if (Type == TEXT("ProgressBar")) WidgetClass = UProgressBar::StaticClass();
		else if (Type == TEXT("TextBlock")) WidgetClass = UTextBlock::StaticClass();
		else if (Type == TEXT("Image")) WidgetClass = UImage::StaticClass();
		// 可以添加更多类型...
		
		if (!WidgetClass)
		{
			UE_LOG(LogTemp, Warning, TEXT("CreateWidgetsFromJson: Unknown widget type %s"), *Type);
			return nullptr;
		}
		
		// 创建控件
		UWidget* NewWidget = WidgetBlueprint->WidgetTree->ConstructWidget<UWidget>(WidgetClass, FName(*Name));
		if (!NewWidget)
		{
			UE_LOG(LogTemp, Warning, TEXT("CreateWidgetsFromJson: Failed to create widget %s"), *Name);
			return nullptr;
		}
		
		UE_LOG(LogTemp, Log, TEXT("CreateWidgetsFromJson: Created %s (%s)"), *Name, *Type);
		
		// 如果有父控件，添加到父控件
		if (Parent)
		{
			UPanelWidget* PanelParent = Cast<UPanelWidget>(Parent);
			if (PanelParent)
			{
				PanelParent->AddChild(NewWidget);
			}
		}
		
		// 处理子控件
		const TArray<TSharedPtr<FJsonValue>>* ChildrenArray;
		if (CompDef->TryGetArrayField(TEXT("children"), ChildrenArray))
		{
			for (const TSharedPtr<FJsonValue>& ChildValue : *ChildrenArray)
			{
				const TSharedPtr<FJsonObject>* ChildObj;
				if (ChildValue->TryGetObject(ChildObj))
				{
					CreateWidgetRecursive(*ChildObj, NewWidget);
				}
			}
		}
		
		return NewWidget;
	};
	
	// 创建所有根级组件
	UWidget* FirstRoot = nullptr;
	for (const TSharedPtr<FJsonValue>& CompValue : *ComponentsArray)
	{
		const TSharedPtr<FJsonObject>* CompObj;
		if (CompValue->TryGetObject(CompObj))
		{
			UWidget* RootWidget = CreateWidgetRecursive(*CompObj, nullptr);
			if (!FirstRoot && RootWidget)
			{
				FirstRoot = RootWidget;
			}
		}
	}
	
	// 设置第一个为根控件
	if (FirstRoot)
	{
		WidgetBlueprint->WidgetTree->RootWidget = FirstRoot;
		UE_LOG(LogTemp, Log, TEXT("CreateWidgetsFromJson: Set root widget to %s"), *FirstRoot->GetName());
	}
	
	return true;
}
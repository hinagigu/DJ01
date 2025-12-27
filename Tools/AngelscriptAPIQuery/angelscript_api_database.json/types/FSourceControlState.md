# FSourceControlState

Snapshot of source control state of a file
@see        USourceControlHelpers::QueryFileState()

## 属性

### Filename
- **类型**: `FString`
- **描述**: Get the local filename that this state represents

### bIsValid
- **类型**: `bool`
- **描述**: Indicates whether this source control state has valid information (true) or not (false)

### bIsUnknown
- **类型**: `bool`
- **描述**: Determine if we know anything about the source control state of this file

### bCanCheckIn
- **类型**: `bool`
- **描述**: Determine if this file can be checked in.

### bCanCheckOut
- **类型**: `bool`
- **描述**: Determine if this file can be checked out

### bIsCheckedOut
- **类型**: `bool`
- **描述**: Determine if this file is checked out

### bIsCurrent
- **类型**: `bool`
- **描述**: Determine if this file is up-to-date with the version in source control

### bIsSourceControlled
- **类型**: `bool`
- **描述**: Determine if this file is under source control

### bIsAdded
- **类型**: `bool`
- **描述**: Determine if this file is marked for add
@note        if already checked in then not considered mid add

### bIsDeleted
- **类型**: `bool`
- **描述**: Determine if this file is marked for delete

### bIsIgnored
- **类型**: `bool`
- **描述**: Determine if this file is ignored by source control

### bCanEdit
- **类型**: `bool`
- **描述**: Determine if source control allows this file to be edited

### bCanDelete
- **类型**: `bool`
- **描述**: Determine if source control allows this file to be deleted.

### bIsModified
- **类型**: `bool`
- **描述**: Determine if this file is modified compared to the version in source control.

### bCanAdd
- **类型**: `bool`
- **描述**: Determine if this file can be added to source control (i.e. is part of the directory
structure currently under source control)

### bIsConflicted
- **类型**: `bool`
- **描述**: Determine if this file is in a conflicted state

### bCanRevert
- **类型**: `bool`
- **描述**: Determine if this file can be reverted, i.e. discard changes and the file will no longer be checked-out.

### bIsCheckedOutOther
- **类型**: `bool`
- **描述**: Determine if this file is checked out by someone else

### CheckedOutOther
- **类型**: `FString`
- **描述**: Get name of other user who this file already checked out or "" if no other user has it checked out

## 方法

### opAssign
```angelscript
FSourceControlState& opAssign(FSourceControlState Other)
```


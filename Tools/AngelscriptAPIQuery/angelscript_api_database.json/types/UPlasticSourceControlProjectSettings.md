# UPlasticSourceControlProjectSettings

**继承自**: `UDeveloperSettings`

Project Settings for Unity Version Control (formerly Plastic SCM). Saved in Config/DefaultEditor.ini

## 属性

### UserNameToDisplayName
- **类型**: `TMap<FString,FString>`
- **描述**: Map Unity Version Control user names (typically e-mail addresses or company domain names) to display names for brevity.

### bHideEmailDomainInUsername
- **类型**: `bool`
- **描述**: Hide the domain part of an username e-mail address (eg @gmail.com) if the UserNameToDisplayName map didn't match (enabled by default).

### bPromptForCheckoutOnChange
- **类型**: `bool`
- **描述**: If enabled, you'll be prompted to check out changed files (enabled by default). Checkout is needed to work with Changelists.

### LimitNumberOfRevisionsInHistory
- **类型**: `int`
- **描述**: If a non-null value is set, limit the maximum number of revisions requested to Unity Version Control to display in the "History" window.

### bShowBranchRepositoryColumn
- **类型**: `bool`
- **描述**: Show the repository when the branch is created (hidden by default)

### bShowBranchCreatedByColumn
- **类型**: `bool`
- **描述**: Show the name of the creator of the branch

### bShowBranchDateColumn
- **类型**: `bool`
- **描述**: Show the date of creation of the branch

### bShowBranchCommentColumn
- **类型**: `bool`
- **描述**: Show the comment of the branch


# UEditableGameplayTagQuery

**继承自**: `UObject`

This is an editor-only representation of a query, designed to be editable with a typical property window.
To edit a query in the editor, an FGameplayTagQuery is converted to a set of UObjects and edited,  When finished,
the query struct is rewritten and these UObjects are discarded.
This query representation is not intended for runtime use.

## 属性

### UserDescription
- **类型**: `FString`
- **描述**: User-supplied description, shown in property details. Auto-generated description is shown if not supplied.

### RootExpression
- **类型**: `UEditableGameplayTagQueryExpression`
- **描述**: The base expression of this query.


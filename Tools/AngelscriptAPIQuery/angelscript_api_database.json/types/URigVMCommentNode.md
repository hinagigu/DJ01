# URigVMCommentNode

**继承自**: `URigVMNode`

Comment Nodes can be used to annotate a Graph by adding
colored grouping as well as user provided text.
Comment Nodes are purely cosmetic and don't contribute
to the runtime result of the Graph / Function.

## 方法

### GetCommentBubbleVisible
```angelscript
bool GetCommentBubbleVisible()
```
Returns the current user provided bubble visibility of this comment.

### GetCommentColorBubble
```angelscript
bool GetCommentColorBubble()
```
Returns the current user provided bubble color inheritance of this comment.

### GetCommentFontSize
```angelscript
int GetCommentFontSize()
```
Returns the current user provided font size of this comment.

### GetCommentText
```angelscript
FString GetCommentText()
```
Returns the current user provided text of this comment.


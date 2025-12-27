# UBTComposite_Sequence

**继承自**: `UBTCompositeNode`

Sequence composite node.
Sequence Nodes execute their children from left to right, and will stop executing its children when one of their children fails.
If a child fails, then the Sequence fails. If all the Sequence's children succeed, then the Sequence succeeds.


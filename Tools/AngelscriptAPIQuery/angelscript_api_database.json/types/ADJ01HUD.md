# ADJ01HUD

**继承自**: `AHUD`

DJ01 HUD类

游戏的主HUD类，负责：
- 管理UI布局层
- 提供UI扩展点
- 处理GameFeature添加的UI元素

使用方式：
1. 在GameMode中设置此类为HUD类
2. GameFeatureAction_AddWidgets会向此HUD添加UI


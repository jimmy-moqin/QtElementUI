# Qt-ElementUI
## 简介
这是一个正在开发中的PyQt UI库，界面设计仿照ElementUI，以尽量复刻其样式和响应状态为目标，同时也增添了几个在C端常用的组件。
ps：组件命名与ElementUI风格一致，例如ElButton、ElInput等
## 特性
1. 本项目使用scss预处理器对样式进行预处理，旨在节省样式设计时的时间。因为Qss样式表实际上可以等同于CSS 2.1，故此scss预处理器完全可以胜任对qss的编译。
2. 本项目的设计理念是：UI与逻辑分离，这样一种常规的解耦思想。因此在设计组件时，会优先考虑组件样式能否在qss中设置，而不是全在逻辑代码中修改。以此最大限度地与现有项目兼容。
3. 易于修改，对ElementUI熟悉的开发者来说，修改ElementUI的默认样式极其困难。本项目力争改进这种现状，尽可能少的嵌套控件，尽量使用原生控件加样式修改的方式实现。
## 预览
一下是目前已经做好的几种组件
1. **ElButton**

    <img src=".\resource\img\button_show.png" alt="catalog_show" style="zoom:67%;" />

2. **ElCatalog**

    <img src=".\resource\img\catalog_show.png" alt="catalog_show" style="zoom:67%;" />

3. **ElInput**

    <img src=".\resource\img\input_show.png" alt="catalog_show" style="zoom:67%;" />
## 鸣谢
感谢zhiyiYo的[PyQt Fluent UI](https://github.com/zhiyiYo/PyQt-Fluent-Widgets)优秀项目，给了我开发本项目的启发与技术参考，请给他Star！
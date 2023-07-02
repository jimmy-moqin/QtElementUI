# Qt-ElementUI

[简体中文](README_zh.md)

## UpDate
ElTable Component

## Introduction
This is a PyQt UI library under development. The interface design is modeled after ElementUI, with the goal of replicating its style and responsiveness as much as possible, while also adding several components commonly used in the C-side.
ps: the components are named in the same style as ElementUI, e.g. ElButton, ElInput, etc.

## Features
1. This project uses the scss preprocessor to pre-process the styles, in order to save time when designing the styles. As Qss style sheets are effectively equivalent to CSS 2.1, the scss preprocessor is fully capable of compiling qss. 2.
2. The design philosophy of this project is to separate the UI from the logic, a conventional decoupling idea. Therefore, when designing components, priority is given to whether the component styles can be set in qss, rather than modified in the logic code. This is to maximise compatibility with existing projects. 3.
3. easy to modify, it is extremely difficult for developers familiar with ElementUI to modify the default style of ElementUI. This project strives to improve this situation by nesting as few controls as possible and using native controls plus style modifications as much as possible to achieve this.

## Preview
Here are a few of the components that have been done so far
1. **ElButton**

   <img src=".\resource\img\button_show.png" alt="catalog_show" style="zoom:67%;" />

2. **ElCatalog**

    <img src=".\resource\img\catalog_show.png" alt="catalog_show" style="zoom:67%;" />

3. **ElInput**

    <img src=".\resource\img\input_show.png" alt="catalog_show" style="zoom:67%;" />
## Acknowledgements
Thanks to zhiyiYo's [PyQt Fluent UI](https://github.com/zhiyiYo/PyQt-Fluent-Widgets) excellent project that gave me inspiration and technical reference to develop this project, please give him Star!

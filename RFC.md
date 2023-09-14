# 程序设计文档
## 主体逻辑
### 玩家飞机
#### 飞机生成
设置生成的初始位置、图片等等
#### 飞机重生
飞机死亡后，在初始位置重生，拥有一定无敌帧；同时生命值减一
#### 飞机移动
飞机可以上下左右移动，但是不能超过屏幕范围，也要留出屏幕下方炸弹和生命值的区域
#### 发射子弹
飞机可以自动发射子弹，需要限制子弹生成的速度
#### 补给品
飞机获得炸弹时，增加炸弹的数量，同时限制炸弹最多拥有的数量；飞机获得双倍子弹时，切换发射的子弹，但是有时间限制

### 敌机
#### 生成
大、中、小生成事件不一致，生成时间可以随着难度缩短，生成位置在屏幕上方之外
#### 移动
敌机垂直向下移动，移动速度可以随难度增加
#### 摧毁
大、中、小飞机摧毁需要的子弹不一样，参数控制，有相应的受击和坠毁的动画

### 补给品
#### 生成
每30秒随机生成炸弹或者超级子弹，生成位置在屏幕上方之外
#### 移动
垂直向下移动

### 界面控制
1. 需要标识重置游戏（重置游戏、开始都进入一个界面）、结束游戏（手动结束、或者死亡结束进入同一个界面），重置游戏和结束游戏相互切换
2. 暂停与非暂停相互切换
3. 游戏默认进入开始界面，处于非运行状态、非暂停状态。点击开始游戏后，处于运行状态、非暂停状态。即用两个参数控制游戏是否运行，以及处于的界面
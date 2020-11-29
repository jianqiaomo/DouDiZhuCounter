## 三人斗地主计分器

如果你在玩纸牌版三人斗地主，但是觉得炸弹、春天、抢地主翻倍，还有大家的总分计算起来很麻烦，不妨试一下这个小脚本。

每局打完后，向控制台输入本局的炸弹个数、抢地主次数、春天，再输入最后赢家，即可记录下大家的分数。

### 示例
- `python count.py`

    <div align="center">
      <img src="https://github.com/jianqiaomo/DouDiZhuCounter/blob/master/example1.png?raw=true"/>
    </div>
    
    - 第一个 _**2**_ 3 
        - 表示可能发生了一次抢地主和一次炸弹(翻倍 **_2_** 次)，三号玩家地主胜利，
        - 赚 2(默认底分)* [ 2 ^ **_2_** (抢地主+炸弹) ] = 8
    - 第二个 0 1 2 
        - 表示没有抢地主，也没有发生炸弹，一号二号玩家农民胜利
        - 地主扣 2(默认底分) 平分给农民


- 不小心输入错误?  输入`recall`回到上一次的结果。

- 想改变默认底分?  开始时输入`setup` `yes` 设置数值。
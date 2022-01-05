# Oscillator-system

######################################
Writed by Xie Shangyan (Shane) in 801, T6 Buliding,
Harbin Institute of Technology, Shenzhen, China.
Time: 2022-01-05
######################################

This part is associated with a nonlinear oscillate system to test PPO.

The oscillator system is,
a1(dot) = 0.1*a1 - a2;
a2(dot) = 0.1*a2 + a1 +b.

Intitial condition:
a1(0) = 1;
a2(0) =0.

Minimize cost:
J = a1^2 +a2^2 + 0.01b^2


Using method:
1-Modify the path to adpate your computer;
2-Load "oscillator.py";
3-Run "oscillator_main.py".


Version:
Python 3.8.2

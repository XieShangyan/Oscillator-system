import numpy as np
import time
import sys
import math


class env:
    def __init__(self):
        self.a1 = 1
        self.a2 = 0
        self.n_features = 2
        self.step_num = 0
        self.b = 0
        self.his_b = [self.b]
        self.his_a1 = [self.a1]
        self.his_a2 = [self.a2]
        self.n_actions = 1


    def reset(self):
        self.a1 = 1
        self.a2 = 0
        self.step_num = 0
        self.b = 0
        self.his_b = [self.b]
        self.his_a1 = [self.a1]
        self.his_a2 = [self.a2]
        return np.array([self.a1, self.a2])

    def step(self, action):
        self.step_num += 1
        tmp_a1 = 0.1 * self.a1 - self.a2
        tmp_a2 = 0.1 * self.a2 + self.a1 + action[0]
        s = np.array([self.a1, self.a2])
        self.a1 = tmp_a1
        self.a2 = tmp_a2
        s_ = np.array([self.a1, self.a2])
        self.his_a1.append(tmp_a1)
        self.his_a2.append(tmp_a2)
        self.his_b.append(action[0])
        reward = 0
        tmp_reward_a1a2 = 0
        tmp_reward_b = 0
        for i, item in enumerate(self.his_a1):
            tmp_reward_a1a2 += item * item
            tmp_reward_a1a2 += self.his_a2[i] * self.his_a2[i]
            tmp_reward_b += self.his_b[i] * self.his_b[i]
        tmp_reward_a1a2 /= len(self.his_a1)
        tmp_reward_b /= 0.01 * len(self.his_a1)
        reward = 1.2 - tmp_reward_a1a2 - tmp_reward_b
        done = False
        if reward < -10:
            done = True
        return s_, reward, done, s
 
   

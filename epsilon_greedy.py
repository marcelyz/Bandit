import numpy as np

T = 100000  # T个客人
N = 10  # N道菜

true_rewards = np.random.uniform(low=0, high=1, size=N)  # N道菜好吃的概率
estimated_rewards = np.zeros(N)
number_of_trials = np.zeros(N)
total_reward = 0


def alpha_greedy(N, alpha=0.1):
    item = 0
    if np.random.random() < alpha:
        item = np.random.randint(low=0, high=N)
    else:
        item = np.argmax(estimated_rewards)
    reward = np.random.binomial(n=1, p=true_rewards[item])
    return item, reward


for t in range(1, T):  # T个客人依次进入餐馆
    # 从N道菜中推荐一个，reward = 1 表示客人接受，reward = 0 表示客人拒绝并离开
    item, reward = alpha_greedy(N)
    total_reward += reward  # 一共有多少客人接受了推荐

    # 更新菜的平均成功概率
    number_of_trials[item] += 1
    estimated_rewards[item] = ((number_of_trials[item] - 1) * estimated_rewards[item] + reward) / number_of_trials[item]

print("total_reward=" + str(total_reward))
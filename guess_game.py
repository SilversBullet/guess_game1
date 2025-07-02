import streamlit as st
import random

# --- 游戏初始化 ---
# st.session_state 是Streamlit提供的“会话状态”对象，用来在多次交互之间保存变量。
# 我们用它来存储 secret_number，确保它在整个游戏会话中保持不变。

# 检查 'secret_number' 是否已经存在于 session_state 中
# 如果不存在，说明是游戏刚开始，我们需要生成一个新的秘密数字
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)

# --- 网页界面布局 ---

# 1. 显示标题和游戏说明
st.title(" 猜数字游戏 🎮")
st.write("我心里想好了一个 1 到 100 之间的数字，你来猜猜看吧！")

# 2. 创建一个数字输入框，让用户输入猜测的数字
# 使用 st.number_input 可以确保用户输入的是数字
# step=1 表示每次点击加减号，数字变化1
# value=None 让输入框默认为空
guess = st.number_input("请输入你猜的数字:", min_value=1, max_value=100, step=1, value=None)

# 3. 创建一个“猜！”按钮
# 我们把主要的游戏判断逻辑放在这个 if 语句块里
# 只有当用户点击按钮时，才会执行判断
if st.button("猜！"):
    # 检查用户是否输入了数字
    if guess is None:
        st.warning("你还没有输入数字哦！")
    else:
        # 获取存储在 session_state 中的秘密数字
        secret_number = st.session_state.secret_number
        
        # --- 核心判断逻辑 ---
        if guess < secret_number:
            st.info("太小了，再往大点猜！") # st.info() 显示一个蓝色的提示框
        elif guess > secret_number:
            st.info("太大了，再往小点猜！")
        else:
            st.success(f"🎉 恭喜你！猜对了！就是数字 {secret_number}！🎉")
            st.balloons() # 猜对了，放点气球庆祝一下！
            
            # 游戏结束后，可以重置秘密数字，以便开始新一轮游戏
            # 这里我们通过删除 session_state 中的 key 来实现
            del st.session_state.secret_number
            st.write("我已经想好了下一个数字，刷新页面或者再次输入来开始新游戏吧！")

# 为了增加趣味性，可以添加一个“重置游戏”的按钮
if st.button("重置游戏并换个数字"):
    st.session_state.secret_number = random.randint(1, 100)
    st.rerun() # 立即重新运行整个脚本，刷新界面
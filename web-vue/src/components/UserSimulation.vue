<template>
  <el-container>
    <el-main>
      <h1>用户模拟</h1>
      <p>我们通过随机抽取二手车交易记录数据中的一部分数据（500条）来作为一个用户的浏览记录数据，从而针对该用户建立起用户画像。具体分析过程如下：</p>
      
      <div class="image-section">
        <h2>用户偏好分析-品牌占比</h2>
        <img src="@/assets/用户品牌.jpg" alt="用户品牌">
        <div><a href="/品牌偏好.html" target="_blank">具体呈现</a></div>
      </div>

      <div class="image-section">
        <h2>用户偏好分析-车型占比</h2>
        <img src="@/assets/用户车型.jpg" alt="用户车型">
        <div><a href="/车型偏好.html" target="_blank">具体呈现</a></div>
      </div>

      <div class="image-section">
        <h2>用户偏好分析-价格区间</h2>
        <img src="@/assets/用户价格.jpg" alt="用户价格">
        <div><a href="/价格偏好.html" target="_blank">具体呈现</a></div>
      </div>

      <div class="image-section">
        <h2>用户画像</h2>
        <img src="@/assets/用户画像.jpg" alt="用户画像">
      </div>

      <h2>结论</h2>
      <p>我们利用500条数据来模拟一位用户的点击和搜索记录，通过分析可以得出，用户最喜欢的浏览的品牌是揽胜极光，更喜欢豪华轿车车型，偏向购买价格较低，理想区间0-10000，性价比高的二手车车辆。</p>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'UserSimulation',
}
</script>

<style scoped>
h1 {
  margin-top: 20px;
}

h2 {
  margin-top: 20px;
}

p {
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 20px;
}

.image-section {
  margin-bottom: 20px;
}

.image-section img {
  width: 70%;
  height: auto;
}
</style>

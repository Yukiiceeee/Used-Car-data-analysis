<template>
  <el-container>
    <el-main>
      <h1>品牌汽车价格离群值</h1>
      <p class="centered">我们通过分析不同品牌二手车价格的离群值情况，利用箱线图作为可视化工具，帮助用户快速识别哪些品牌的二手车价格存在异常波动。通过对数据集的探索，我们可以更好地理解市场情况，为二手车买卖提供参考。具体分析如下：</p>
      
      <div class="image-section">
        <h2>不同品牌价格离群值</h2>
        <img src="@/assets/二手车品牌箱线图.jpg" alt="二手车品牌箱线图">
      </div>

      <h2>结论</h2>
      <p class="centered">利用箱线图对不同品牌二手车价格的离群值情况进行了可视化分析。通过对比不同品牌的箱线图，我们可以快速识别哪些品牌的二手车价格存在异常波动，为二手车买卖提供参考。</p>
      <p class="centered">同时，也为二手车市场的价格分析和策略制定提供了一定的参考依据。对于消费者而言，在购买二手车时，可以结合箱线图的分析结果，选择价格相对稳定、波动较小的品牌，以降低购买风险。对于二手车商而言，可以根据箱线图的分析结果，调整不同品牌二手车的定价策略，以更好地满足市场需求。</p>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'BrandPriceTrends',
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

.centered {
}

.image-section {
  margin-bottom: 20px;
}

.image-section img {
  width: 70%;
  height: auto;
}
</style>

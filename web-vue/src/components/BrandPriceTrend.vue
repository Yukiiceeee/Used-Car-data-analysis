<template>
  <el-container>
    <el-main>
      <h1>品牌汽车价格变化趋势</h1>
      <p>我们通过对不同品牌、不同车型汽车销售价格随时间的变化情况，对其进行价格随时间变化趋势的分析。具体分析如下：</p>
      
      <div class="section">
        <h2>不同品牌价格变化趋势</h2>
        <div class="image-row">
          <img src="@/assets/品牌趋势1.jpg" alt="品牌趋势1" class="image-small">
          <img src="@/assets/品牌趋势2.jpg" alt="品牌趋势2" class="image-small">
        </div>
      </div>
      
      <div class="section">
        <h2>不同车型价格变化趋势</h2>
        <div class="image-row">
          <img src="@/assets/车型趋势1.jpg" alt="车型趋势1" class="image-small">
          <img src="@/assets/车型趋势2.jpg" alt="车型趋势2" class="image-small">
        </div>
      </div>
      
      <h2>结论</h2>
      <p>依照图表，针对品牌，我们不难看出Panamera的价格在2015年12月附近有所降低，但在此之后马上就有了一次回升，而且在后期仍然会有走高；宝马3系价格在2016年3月附近有明显上升，而且在不远的未来一定会再有一次明显上升（暂以此两品牌为例）。</p>
      <p>针对车型，我们不难看出厢式车的市场价格在2015年11月的中旬有一次较大的下跌，随后是一次小回升，在2016年3月有一次较小的下跌，预计在未来会再有一次小回升；双面汽车的市场价格在2016年2月有一次较小的下跌，随后是一次较大回升，在2016年3，4月价格较为平稳，预计在未来会再有一次小下跌。</p>
      
      <div class="section">
        <h2>二手车交易价格变化与未来预测</h2>
        <img src="@/assets/价格随时间预测.jpg" alt="价格随时间预测" class="image-large">
      </div>
      
      <h2>结论</h2>
      <p>展示2016年3月二手车的价格走势，可以看出，二手车价格呈现出一定的波动趋势，但整体而言，价格相对稳定。然后，我们在同一张图上绘制了预测价格的折线图，以便对比实际价格和预测价格，这里采用了简单的线性回归模型作为预测方法，通过将销售日期转换为从月初开始的天数，我们训练了一个线性回归模型，并基于该模型预测了未来一个月的二手车价格。通过对比，我们可以清晰地看到价格的变化趋势和预测结果，由于只有一个月的数据用于训练模型，预测结果可能存在一定的误差。</p>
      <p>根据预测结果，如果消费者计划在近期购买二手车，可以考虑在价格相对较低时入手。但请注意，购买决策应综合考虑多个因素，如车型、车况、里程数等。虽然预测结果可能存在一定的误差，但通过数据可视化和模型优化等方法，我们可以不断提高预测的准确性，为二手车市场的发展和消费者的购买决策提供更多的支持。</p>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'BrandPriceTrends',
}
</script>

<style scoped>
h1, h2 {
  margin-top: 20px;
  text-align: left;
}

p {
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 20px;
  text-align: left;
}

.image-small {
  width: 45%; /* 调整图片的宽度 */
  height: auto;
  margin-right: 10px; /* 添加右边距 */
}

.image-large {
  width: 70%; /* 调整图片的宽度为70% */
  height: auto;
  display: block;
  margin: 0 auto;
}

.image-row {
  display: flex;
  justify-content: flex-start; /* 确保图片左对齐 */
  align-items: center;
  margin-bottom: 20px;
}

.section {
  margin-bottom: 20px;
}
</style>

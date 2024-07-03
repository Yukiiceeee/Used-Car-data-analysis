<template>
  <el-container>
    <el-main>
      <h1>销售季时间序列分析</h1>
      <p>为了展示二手车交易的旺季与乏季，我们选取了一个时间段的交易记录，并对其进行了时间序列分析，分析结果如下：</p>
      
      <h2>二手车交易的时间序列分析</h2>
      <img src="@/assets/时间序列分析.jpg" alt="二手车交易的时间序列分析" class="responsive-image">
      
      <h3>结论</h3>
      <p>
        从分析结果可以看出，总体上每天的销售量都较高，变化不大，头尾出现几个异常值，可能是数据量不足导致的，主要是2016-03-13和2016-03-18这两天的销售量与临近日期相差较大。
        后续，可以针对时间序列销售数据，建立基于时间对销售量预估的预测模型。
      </p>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'TimeSeriesAnalysis'
}
</script>

<style scoped>
h1, h2, h3 {
  margin-top: 20px;
}

p {
  font-size: 16px;
  line-height: 1.6;
}

.responsive-image {
  width: 70%;  /* Set the width to 70% of container width */
  height: auto; /* Maintain aspect ratio */
  display: block;
  margin-left: auto;
  margin-right: auto; /* Center the image horizontally */
}
</style>

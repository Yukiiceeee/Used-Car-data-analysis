<template>
  <el-container>
    <el-main>
      <h1>不同类型车辆受欢迎度</h1>
      <p>我们分析了不同车型、不同燃油类型、不同品牌汽车的受欢迎程度（以交易记录数为衡量依据），结果如下：</p>
      
      <h2>不同车型的受欢迎程度对比</h2>
      <img src="@/assets/车型.jpg" alt="不同车型的受欢迎程度对比" class="responsive-image">
      
      <h2>不同燃油类型的受欢迎程度对比</h2>
      <img src="@/assets/燃油类型.jpg" alt="不同燃油类型的受欢迎程度对比" class="responsive-image">
      
      <h2>不同品牌汽车的受欢迎程度对比</h2>
      <img src="@/assets/品牌.jpg" alt="不同品牌汽车的受欢迎程度对比" class="responsive-image">
      
      <h3>结论</h3>
      <p>
        从分析结果可以看出，微型车、厢型车、豪华轿车的受欢迎程度较高，汽油、柴油的受欢迎程度较高（或较为普遍），揽胜极光品牌的受欢迎程度较高。
        企业在进行决策时，可以考虑更多地购进如上汽车属性的二手车车辆。
        但分析也有些不足之处：仅用交易数据衡量，没有参考评分等数据，可能仅仅是因为该属性车辆较为普遍，从而丧失了对受欢迎程度的一定程度上的区分度。
      </p>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'VehiclePopularity'
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
  margin-right: auto; /* Center the image horizontally */
}
</style>

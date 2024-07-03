<template>
  <el-container>
    <el-main>
      <h1>车辆属性与价格之间的关系</h1>
      <p>
        我们选取了交易记录数最多的6个品牌，以及交易记录数最多的6个车型进行相关分析，统计了品牌、车型与价格之间的关系，结果如下：
      </p>
      
      <h2>品牌与价格之间的关系</h2>
      <img src="@/assets/品牌与价格关系.jpg" alt="品牌与价格关系" class="responsive-image">
      <div><a href="/Top6_brand_价格关系.html" target="_blank">具体呈现</a></div>

      <h2>车型与价格之间的关系</h2>
      <img src="@/assets/车型与价格关系.jpg" alt="车型与价格关系" class="responsive-image">
      <div><a href="/Top6_bodyType_价格关系.html" target="_blank">具体呈现</a></div>

      <h3>结论</h3>
      <p>揽胜极光品牌的二手车价格相对更高，跑车、商务车、大巴车三种车型的价格相对更高。</p>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'VehiclePriceRelationship'
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
  width: 70%;  /* Adjust the width to resize the images */
  height: auto; /* Maintain aspect ratio */
  display: block;
}
</style>

<template>
  <el-container>
    <el-main>
      <h1>车辆性价比分析</h1>
      <p>为了使用户能够更好地以较低的价格买到品质更优的车辆，我们通过现有的二手车交易记录，对其车辆的性价比进行了相关分析。具体分析如下：</p>
      <div class="section">
        <h2>是否损坏，使用时间对价格影响</h2>
        <div class="image-row">
          <img src="@/assets/性价比1.jpg" alt="性价比1" class="image-small">
          <img src="@/assets/性价比2.jpg" alt="性价比2" class="image-small">
        </div>
        <div class="image-row">
          <img src="@/assets/性价比3.jpg" alt="性价比3" class="image-small">
          <img src="@/assets/性价比4.jpg" alt="性价比4" class="image-small">
        </div>
      </div>
      
      <h2>结论</h2>
      <p>相同品牌、车型、燃油类型情况下，随使用时间增长，价格逐渐变低；是否受损对价格降低的趋势影响幅度也有差异。而当品牌、车型、燃油类型不同时，随使用时间增长，价格逐渐变低的规律不变，但是否受损对价格影响的幅度会有所不同。</p>
      
      <div class="section">
        <h2>性能评分与价格之间关系</h2>
        <img src="@/assets/性能价格关系.jpg" alt="性能价格关系" class="image-small">
      </div>
      
      <div class="section">
        <h2>各品牌、车型性价比评分</h2>
        <img src="@/assets/性价比.jpg" alt="性价比" class="image-small">
        <div><a href="/bar3d_brand_bodytype_scores1.html" target="_blank">具体呈现</a></div>
        <div><a href="/bar3d_brand_fueltype_scores1.html" target="_blank">具体呈现</a></div>
      </div>
      
      <h2>结论</h2>
      <p>通过性价比3D分析图，可以得到：</p>
      <p>豪华轿车性价比最高的品牌是奥迪A6L，其总评分为433分。</p>
      <p>厢式车性价比最高的品牌是揽胜极光，其总评分为557分。</p>
      <p>敞篷车性价比最高的品牌是蒙迪欧，其总评分为333分。</p>
      <p>商务车性价比最高的品牌是奔驰C级，其总评分为386分。</p>
      <p>故而，用户可以基于这些分析结论，帮助自己更好地购买二手车车辆。</p>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'CostPerformanceAnalysis',
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
  margin-bottom: 20px; /* 添加底部边距 */
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

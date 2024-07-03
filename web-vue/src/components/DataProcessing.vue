<template>
  <el-container>
    <el-main>
      <h2>描述性统计</h2>
      <!-- 使用静态图片显示描述性统计 -->
      <img src="@/assets/描述性统计.jpg" alt="描述性统计图表" style="width: 100%; height: auto;">

      <div class="section">
        <h2>数据清洗</h2>
        <div class="image-section">
          <h3>异常值处理前后-公里数、马力和价格的箱线图对比</h3>
          <div class="boxplot-row">
            <img src="@/assets/kilometer.png" alt="Kilometer">
            <img src="@/assets/power.png" alt="Power">
            <img src="@/assets/price.png" alt="Price">
          </div>
          <h3>异常值处理前后-公里数、马力和价格的分布直方图对比</h3>
          <div class="comparison-row">
            <img src="@/assets/原始数据.png" alt="Original Data">
            <img src="@/assets/异常值处理后.png" alt="Data After Cleaning">
          </div>
        </div>
      </div>

      <h2>缺失值处理</h2>
      <el-card class="box-card">
        <div slot="header" class="clearfix">
          <span>缺失值处理信息</span>
        </div>
        <el-table :data="missingData" style="width: 100%" border stripe>
          <el-table-column prop="field" label="字段" width="180"></el-table-column>
          <el-table-column prop="missingCount" label="缺失值数量" width="180"></el-table-column>
          <el-table-column prop="action" label="处理措施"></el-table-column>
        </el-table>
      </el-card>
    </el-main>
  </el-container>
</template>

<script>
export default {
  name: 'DataPreprocessing',
  data() {
    return {
      missingData: [
        { field: "notRepairedDamage", missingCount: "24324", action: "填补为‘未知’" },
        { field: "fuelType", missingCount: "8680", action: "填补为‘未知’" },
        { field: "gearbox", missingCount: "5981", action: "填补为‘未知’" },
        { field: "bodyType", missingCount: "4506", action: "填补为‘未知’" },
        { field: "model", missingCount: "1", action: "直接删除" }
      ]
    };
  }
}
</script>

<style scoped>
h2, h3 {
  margin-top: 20px;
}

.image-section h3 {
  margin-bottom: 10px;
}

.boxplot-row, .comparison-row {
  display: flex;
  justify-content: space-around; /* Ensures even spacing */
  align-items: center; /* Vertically centers items in the container */
  margin-bottom: 20px; /* Adds space below the row */
}

.boxplot-row img, .comparison-row img {
  width: 49%; /* Adjusts width for the images */
  height: auto; /* Maintains aspect ratio */
}

.box-card {
  margin-top: 20px; /* Adds spacing above the card */
}
</style>

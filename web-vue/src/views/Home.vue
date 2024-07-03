<template>
  <div class="home">
    <el-container>
      <el-header style="background-color: #628b97; color: white; text-align: center; padding: 20px;">
        欢迎来到数据分析项目
      </el-header>
      <el-main>
        <p>这是一个基于 Vue 和 Element UI 构建的数据分析项目的主页。在这里，您可以通过左侧的导航菜单访问各种数据分析功能。</p>
        <p>选择“数据预览与查询”开始您的数据探索之旅，或者探索我们的其他分析工具来深入理解市场和消费者趋势。</p>
        <el-button type="primary" @click="goToDataPreview">立即开始探索</el-button>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    goToDataPreview() {
      this.$router.push('/data_preview');
    }
  }
}
</script>

<style scoped>
.home {
  font-family: 'Inter', sans-serif;
}
</style>

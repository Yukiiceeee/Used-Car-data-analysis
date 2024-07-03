<template>
  <div id="app">
    <div class="sidebar">
      <h1>Menu</h1>
      <ul>
        <li><router-link to="/data_preview">数据预览与查询</router-link></li>
        <li><router-link to="/data_processing">数据预处理</router-link></li>
        <li>
          <a href="#" @click="toggleMenu('enterprise')">面向企业分析</a>
          <ul v-show="showEnterpriseMenu">
            <li><router-link to="/vehicle_price">· 车辆属性与价格的关系</router-link></li>
            <li><router-link to="/vehicle_popularity">· 不同类型车辆受欢迎度</router-link></li>
            <li><router-link to="/sales_season">· 销售季时间序列分析</router-link></li>
            <li><router-link to="/user_simulation">· 用户模拟</router-link></li>
            <li><router-link to="/map_visualization">· 地图可视化</router-link></li>
          </ul>
        </li>
        <li>
          <a href="#" @click="toggleMenu('user')"> 面向用户分析</a>
          <ul v-show="showUserMenu">
            <li><router-link to="/brand_price_trend">· 品牌汽车价格变化趋势</router-link></li>
            <li><router-link to="/vehicle_value_for_money">· 车辆性价比分析</router-link></li>
            <li><router-link to="/brand_price_outliers">· 品牌汽车价格离群值</router-link></li>
          </ul>
        </li>
        <li><router-link to="/price_prediction">价格预测</router-link></li>
      </ul>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      showEnterpriseMenu: false,
      showUserMenu: false
    };
  },
  methods: {
    toggleMenu(menu) {
      if (menu === 'enterprise') {
        this.showEnterpriseMenu = !this.showEnterpriseMenu;
      } else if (menu === 'user') {
        this.showUserMenu = !this.showUserMenu;
      }
    }
  }
}
</script>

<style scoped>
body, html {
    font-family: 'Itim', sans-serif;
    height: 100%;
    margin: 0;
    overflow-x: hidden;
}

.sidebar {
    font-family: 'ZCOOL KuaiLe', sans-serif;
    height: 100vh;
    width: 250px;
    position: fixed;
    z-index: 100;
    top: 0;
    left: 0;
    background-color: #628b97;
    overflow-x: hidden;
    overflow-y: auto;
    box-shadow: 3px 0 5px 0 rgba(0,0,0,0.5);
}

.sidebar h1 {
    color: white;
    text-align: center;
    font-size: 34px;
    background-color: #4a6c75;
    padding: 20px 0;
    margin: 0;
}

.sidebar ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.sidebar ul li a, .sidebar ul li router-link {
    display: block;
    color: #e8e7e7;
    padding: 15px;
    text-decoration: none;
    font-size: 18px;
    transition: color 0.3s;
}

.sidebar ul li a:hover, .sidebar ul li router-link:hover {
    color: white;
}

.sidebar ul li .nested {
    padding-left: 20px; /* 给次级菜单一个左缩进 */
}

.sidebar ul li .nested li a {
    font-size: 10px; /* 次级链接字号小于主菜单 */
    color: #e8e7e7;
}

.sidebar ul li .nested li a:hover {
    background-color: #4a6c75;
    color: white;
}

.content {
    margin-left: 250px;
    padding: 20px;
    height: 100vh;
    overflow-y: auto;
}
</style>

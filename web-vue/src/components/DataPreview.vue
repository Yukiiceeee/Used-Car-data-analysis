<template>
  <el-container>
    <el-header class="header">
      基于二手车交易数据的数据分析决策推荐
    </el-header>
    <el-main>
      <div class="search-bar">
        <el-input placeholder="请输入搜索内容" v-model="input" class="search-input"></el-input>
        <el-button type="primary" icon="el-icon-search" @click="handleSearch">搜索</el-button>
      </div>
      <el-table :data="tableData" style="width: 100%">
        <el-table-column prop="SaleID" label="销售ID" width="100"></el-table-column>
        <el-table-column prop="name" label="名称" width="100"></el-table-column>
        <el-table-column prop="regDate" label="注册日期" width="100"></el-table-column>
        <el-table-column prop="model" label="模型" width="100"></el-table-column>
        <el-table-column prop="brand" label="品牌" width="100"></el-table-column>
        <el-table-column prop="bodyType" label="车身类型" width="100"></el-table-column>
        <el-table-column prop="fuelType" label="燃料类型" width="100"></el-table-column>
        <el-table-column prop="gearbox" label="变速箱" width="100"></el-table-column>
        <el-table-column prop="power" label="马力" width="100"></el-table-column>
        <el-table-column prop="kilometer" label="公里数" width="100"></el-table-column>
        <el-table-column prop="notRepairedDamage" label="未修复的损坏" width="150"></el-table-column>
        <el-table-column prop="regionCode" label="区域代码" width="100"></el-table-column>
        <el-table-column prop="seller" label="卖家" width="100"></el-table-column>
        <el-table-column prop="offerType" label="报价类型" width="100"></el-table-column>
        <el-table-column prop="creatDate" label="创建日期" width="100"></el-table-column>
        <el-table-column prop="price" label="价格" width="100"></el-table-column>
      </el-table>
    </el-main>
  </el-container>
</template>

<script>
import axios from 'axios';
import Papa from 'papaparse'; // 引入PapaParse库

export default {
  name: 'DataPreview',
  data() {
    return {
      input: '',
      tableData: []
    };
  },
  methods: {
    handleSearch() {
      alert('搜索内容: ' + this.input);
    },
    loadTableData() {
      axios.get('/data/懂车帝二手车交易数据.csv', { responseType: 'text' })
        .then(response => {
          // 使用PapaParse解析CSV数据
          Papa.parse(response.data, {
            header: true,
            complete: (results) => {
              this.tableData = results.data;
              console.log(this.tableData); // 调试输出，检查数据格式和内容
            }
          });
        })
        .catch(error => {
          console.error('加载数据失败', error);
        });
    }
  },
  mounted() {
    this.loadTableData();
  }
}
</script>


<style scoped>
.header {
  font-family: 'Inter', sans-serif;
  text-align: center;
  color: white;
  padding: 16px;
  font-size: 24px;
  background-color: #628b97;
}

.search-bar {
  font-family: 'Inter', sans-serif;
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;
}

.search-input {
  font-family: 'Inter', sans-serif;
  width: 300px;
}

body, html {
  font-family: 'Inter', sans-serif;
}

.sidebar {
  font-family: 'ZCOOL KuaiLe', sans-serif;
  height: 100vh;
  width: 250px;
  position: fixed;
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
  font-size: 20px;
  transition: color 0.3s;
}

.sidebar ul li a:hover, .sidebar ul li router-link:hover {
  color: white;
}

.content {
  margin-left: 250px;
  padding: 20px;
  height: 100vh;
  overflow-y: auto;
}
</style>
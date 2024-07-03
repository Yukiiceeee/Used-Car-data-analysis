// 首先，导入Vue和Router
import Vue from 'vue';
import Router from 'vue-router';

// 导入你的Vue组件
import Home from '../views/Home.vue';
import DataPreview from '../components/DataPreview.vue';
import DataProcessing from '../components/DataProcessing.vue';
import VehiclePrice from '../components/VehiclePrice.vue';
import VehiclePopularity from '../components/VehiclePopularity.vue';
import SalesSeason from '../components/SalesSeason.vue';
import UserSimulation from '../components/UserSimulation.vue';
import MapVisualization from '../components/MapVisualization.vue';
import BrandPriceTrend from '../components/BrandPriceTrend.vue';
import VehicleValueForMoney from '../components/VehicleValueForMoney.vue';
import BrandPriceOutliers from '../components/BrandPriceOutliers.vue';
import UsedCarTrends from '../components/UsedCarTrends.vue';
import PricePrediction from '../components/PricePrediction.vue';

// 告诉Vue使用VueRouter
Vue.use(Router);

// 导出一个新的路由实例
export default new Router({
  mode: 'history', // 使用历史模式避免哈希标签
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/data_preview',
      name: 'DataPreview',
      component: DataPreview
    },
    {
      path: '/data_processing',
      name: 'DataProcessing',
      component: DataProcessing
    },
    {
      path: '/vehicle_price',
      name: 'VehiclePrice',
      component: VehiclePrice
    },
    {
      path: '/vehicle_popularity',
      name: 'VehiclePopularity',
      component: VehiclePopularity
    },
    {
      path: '/sales_season',
      name: 'SalesSeason',
      component: SalesSeason
    },
    {
      path: '/user_simulation',
      name: 'UserSimulation',
      component: UserSimulation
    },
    {
      path: '/map_visualization',
      name: 'MapVisualization',
      component: MapVisualization
    },
    {
      path: '/brand_price_trend',
      name: 'BrandPriceTrend',
      component: BrandPriceTrend
    },
    {
      path: '/vehicle_value_for_money',
      name: 'VehicleValueForMoney',
      component: VehicleValueForMoney
    },
    {
      path: '/brand_price_outliers',
      name: 'BrandPriceOutliers',
      component: BrandPriceOutliers
    },
    {
      path: '/used_car_trends',
      name: 'UsedCarTrends',
      component: UsedCarTrends
    },
    {
      path: '/price_prediction',
      name: 'PricePrediction',
      component: PricePrediction
    },
    // 你可以继续添加更多的路由和组件
  ]
});

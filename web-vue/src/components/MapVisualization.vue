<template>
  <div>
    <h1>地图可视化</h1>
    <p>为了展示二手车交易在不同地区的差异性，我们针对二手车交易的区域编码，对不同地域交易记录进行了相关分析，结果如下：</p>
    <h2>地图可视化分析</h2>
    <img src="@/assets/地图.jpg" alt="地图可视化分析" style="width: 70%;">
    <div><a href="/car_map.html" target="_blank">具体呈现</a></div>
    <h2>结论</h2>
    <p>平台上的大部分二手车主要来自东部沿海地区的城市，中部地区的二手车数据较少，西部地区更少，几乎没有。从各个城市的数据中也可以看出，大部分沿海地区城市的二手车数量也相对较多，也有各别中部地区城市的二手车数量较多，比如重庆市。</p>
    <p>从地图中，我们可以清晰地看到二手车数量较多的城市和地区，以及数量较少的城市和地区。这种差异可能反映了不同地区的经济发展水平、消费能力、市场需求等因素。</p>
    <p>企业可以根据这个地图来制定二手车投入市场的策略。例如，对于二手车数量较多的地区，企业可以考虑增加投入量，以满足市场需求；对于二手车数量较少的地区，企业可能需要进一步分析市场需求和潜力，以决定是否投入二手车。</p>
    <p>通过地图可视化展示了各地区的二手车数量，为企业提供了决策支持。实验结果表明，地图可视化是一种直观、有效的数据分析工具，可以帮助企业更好地了解市场情况，制定更加科学的决策。</p>
    <p>建议企业在未来的二手车投入市场过程中，结合更多的数据和信息，如人口数量、收入水平、消费习惯等，来综合分析不同地区的市场需求和潜力，以制定更加精准的市场策略。同时，企业也可以考虑使用其他数据可视化工具和技术来进一步挖掘数据的价值，为企业的发展提供更加有力的支持。</p>
  </div>
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

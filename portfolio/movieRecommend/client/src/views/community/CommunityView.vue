<template>
  <div id="CommunityView">
    커뮤니티
    <br>
    <t-table
      :headers="['Name', 'Email', 'Age', 'Sales']"
      :data="[
        ['Alfonso Bribiesca', 'alfonso@vexilo.com', '31', '$9,999.00'],
        ['Saida Redondo', 'saida@gmail.com', 27, '$124.00'],
      ]">
      </t-table>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
name:'CommunityView',

}
</script>

<style>

</style>
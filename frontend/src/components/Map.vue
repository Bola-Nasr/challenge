<template>
  <div id="map" class="h-96 bg-gray-200 rounded-lg shadow-md mt-4"></div>
</template>

<script>
import { initializeMap, updateMap } from '../utils/mapHelpers';

export default {
  props: ['properties'],
  data() {
    return { map: null };
  },
  mounted() {
    this.map = initializeMap('map');
    this.updateMap();
  },
  watch: {
    properties: 'updateMap',
  },
  methods: {
    updateMap() {
      updateMap(this.map, this.properties);
    },
  },
};
</script>

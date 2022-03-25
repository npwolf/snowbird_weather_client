<template>
<div id="801320552"></div>
</template>

<script>
export default {
  name: "Ad",
  methods: {
    initVariables: function() {
      window._mNHandle = window._mNHandle || {};
      window._mNHandle.queue = window._mNHandle.queue || [];
    },
    loadTag: function() {
      window._mNHandle.queue.push(function() {
        window._mNDetails.loadTag("801320552", "728x90", "A_UNIQUE_ID");
      });
    }
  },
  mounted() {
    this.initVariables();
    this.loadTag();
  }
};
</script>

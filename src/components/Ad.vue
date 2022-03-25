<template>
  <div id="801320552"></div>
</template>

<script>
export default {
  name: "Ad",
  methods: {
    initializeMediaNetAdd: function () {
      try {
        window._mNHandle.queue.push(function () {
          window._mNDetails.loadTag("801320552", "728x90", "801320552");
        });
      }
      catch (error) {
        console.log("media.net", error);
      }
    }
  },
  mounted () {
    this.initializeMediaNetAdd();
  }
};
</script>

<template>
<div class="hero is-dark is-fullheight">
    <div class="hero-body">
      <div class="container is-flex is-flex-direction-column" style="max-width: 1000px;">
        
        <!-- 标题 -->
        <h1 class="title has-text-white has-text-centered">智问demo</h1>

        <!-- 聊天内容 -->
        <div class="box has-background-dark p-4 is-flex-grow-1 is-clipped" 
             style="height: 1000px; overflow-y: auto;">
             
          <!-- 示例消息 -->
          
          <!-- AI 回复 -->
          <div class="notification is-light">
            🤖 你好！我是你的 AI 助手，有什么可以帮助你的吗？
          </div>

          <!-- 用户消息 -->
          <div class="notification is-primary has-text-right">
            你好，能帮我写一段 Vue 代码吗？ 🚀
          </div>

          <!-- AI 回复 -->
          <div class="notification is-light">
            🤖 当然！这里是一个简单的 Vue 组件示例：
            <pre><code>&lt;template&gt;
  &lt;h1&gt;Hello, Vue!&lt;/h1&gt;
&lt;/template&gt;</code></pre>
          </div>

          <!-- 用户消息 -->
          <div class="notification is-primary has-text-right">
            太棒了！谢谢你！ 🎉
          </div>

          <!-- AI 回复 -->
          <div class="notification is-light">
            🤖 不客气！如果有任何问题，随时问我哦 😃
          </div>

        </div>

        <!-- 输入框（静态展示，不可输入） -->
        <div class="field has-addons mt-3">
          <div class="control is-expanded">
            <input 
              class="input" 
              type="text" 
              placeholder="输入消息..." 
              disabled
            />
          </div>
          <div class="control">
            <button class="button is-primary" disabled>
              发送
            </button>
          </div>
        </div>

      </div>
    </div>
  </div>
</template>

<script>

    export default{
        name:"LangChain",
        data(){
            return{

            }
        },

    }

</script>
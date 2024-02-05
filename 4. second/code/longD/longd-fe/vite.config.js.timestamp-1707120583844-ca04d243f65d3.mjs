// vite.config.js
import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "file:///C:/Users/SSAFY/Desktop/Today/vue/longD/longd-fe/node_modules/vite/dist/node/index.js";
import vue from "file:///C:/Users/SSAFY/Desktop/Today/vue/longD/longd-fe/node_modules/@vitejs/plugin-vue/dist/index.mjs";
var __vite_injected_original_import_meta_url = "file:///C:/Users/SSAFY/Desktop/Today/vue/longD/longd-fe/vite.config.js";
var vite_config_default = defineConfig(
  {
    plugins: [vue()],
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", __vite_injected_original_import_meta_url))
      }
    }
  },
  {
    server: {
      proxy: {
        "/recording-java/api": {
          target: "https://localhost:5000/",
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/recording-java\/api/, "")
        }
      }
    }
  }
);
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCJDOlxcXFxVc2Vyc1xcXFxTU0FGWVxcXFxEZXNrdG9wXFxcXFRvZGF5XFxcXHZ1ZVxcXFxsb25nRFxcXFxsb25nZC1mZVwiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9maWxlbmFtZSA9IFwiQzpcXFxcVXNlcnNcXFxcU1NBRllcXFxcRGVza3RvcFxcXFxUb2RheVxcXFx2dWVcXFxcbG9uZ0RcXFxcbG9uZ2QtZmVcXFxcdml0ZS5jb25maWcuanNcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfaW1wb3J0X21ldGFfdXJsID0gXCJmaWxlOi8vL0M6L1VzZXJzL1NTQUZZL0Rlc2t0b3AvVG9kYXkvdnVlL2xvbmdEL2xvbmdkLWZlL3ZpdGUuY29uZmlnLmpzXCI7aW1wb3J0IHsgZmlsZVVSTFRvUGF0aCwgVVJMIH0gZnJvbSAnbm9kZTp1cmwnO1xyXG5cclxuaW1wb3J0IHsgZGVmaW5lQ29uZmlnIH0gZnJvbSAndml0ZSc7XHJcbmltcG9ydCB2dWUgZnJvbSAnQHZpdGVqcy9wbHVnaW4tdnVlJztcclxuXHJcbi8vIGh0dHBzOi8vdml0ZWpzLmRldi9jb25maWcvXHJcbmV4cG9ydCBkZWZhdWx0IGRlZmluZUNvbmZpZyhcclxuICB7XHJcbiAgICBwbHVnaW5zOiBbdnVlKCldLFxyXG4gICAgcmVzb2x2ZToge1xyXG4gICAgICBhbGlhczoge1xyXG4gICAgICAgICdAJzogZmlsZVVSTFRvUGF0aChuZXcgVVJMKCcuL3NyYycsIGltcG9ydC5tZXRhLnVybCkpLFxyXG4gICAgICB9LFxyXG4gICAgfSxcclxuICB9LFxyXG4gIHtcclxuICAgIHNlcnZlcjoge1xyXG4gICAgICBwcm94eToge1xyXG4gICAgICAgICcvcmVjb3JkaW5nLWphdmEvYXBpJzoge1xyXG4gICAgICAgICAgdGFyZ2V0OiAnaHR0cHM6Ly9sb2NhbGhvc3Q6NTAwMC8nLFxyXG4gICAgICAgICAgY2hhbmdlT3JpZ2luOiB0cnVlLFxyXG4gICAgICAgICAgcmV3cml0ZTogcGF0aCA9PiBwYXRoLnJlcGxhY2UoL15cXC9yZWNvcmRpbmctamF2YVxcL2FwaS8sICcnKSxcclxuICAgICAgICB9LFxyXG4gICAgICB9LFxyXG4gICAgfSxcclxuICB9LFxyXG4pO1xyXG4iXSwKICAibWFwcGluZ3MiOiAiO0FBQStVLFNBQVMsZUFBZSxXQUFXO0FBRWxYLFNBQVMsb0JBQW9CO0FBQzdCLE9BQU8sU0FBUztBQUhxTSxJQUFNLDJDQUEyQztBQU10USxJQUFPLHNCQUFRO0FBQUEsRUFDYjtBQUFBLElBQ0UsU0FBUyxDQUFDLElBQUksQ0FBQztBQUFBLElBQ2YsU0FBUztBQUFBLE1BQ1AsT0FBTztBQUFBLFFBQ0wsS0FBSyxjQUFjLElBQUksSUFBSSxTQUFTLHdDQUFlLENBQUM7QUFBQSxNQUN0RDtBQUFBLElBQ0Y7QUFBQSxFQUNGO0FBQUEsRUFDQTtBQUFBLElBQ0UsUUFBUTtBQUFBLE1BQ04sT0FBTztBQUFBLFFBQ0wsdUJBQXVCO0FBQUEsVUFDckIsUUFBUTtBQUFBLFVBQ1IsY0FBYztBQUFBLFVBQ2QsU0FBUyxVQUFRLEtBQUssUUFBUSwwQkFBMEIsRUFBRTtBQUFBLFFBQzVEO0FBQUEsTUFDRjtBQUFBLElBQ0Y7QUFBQSxFQUNGO0FBQ0Y7IiwKICAibmFtZXMiOiBbXQp9Cg==

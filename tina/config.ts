import { defineConfig } from "tinacms";

export default defineConfig({
  branch: "main",
  clientId: null,
  token: null,
  build: {
    outputFolder: "admin",
    publicFolder: "static",
  },
  media: {
    tina: {
      mediaRoot: "images",
      publicFolder: "static",
    },
  },
  schema: {
    collections: [
      {
        name: "posts",
        label: "部落格文章",
        path: "content/posts",
        format: "md",
        fields: [
          {
            type: "string",
            name: "title",
            label: "標題",
            isTitle: true,
            required: true,
          },
          {
            type: "datetime",
            name: "date",
            label: "日期",
            required: true,
          },
          {
            type: "boolean",
            name: "draft",
            label: "草稿",
          },
          {
            type: "string",
            name: "categories",
            label: "分類",
            list: true,
            options: [
              { value: "The Workshop", label: "The Workshop (實作工坊)" },
              { value: "The Observatory", label: "The Observatory (觀星台)" },
            ],
          },
          {
            type: "string",
            name: "tags",
            label: "標籤",
            list: true,
          },
          {
            type: "string",
            name: "description",
            label: "描述",
          },
          {
            type: "string",
            name: "author",
            label: "作者",
          },
          {
            type: "boolean",
            name: "ShowReadingTime",
            label: "顯示閱讀時間",
          },
          {
            type: "rich-text",
            name: "body",
            label: "內文",
            isBody: true,
            toolbarOverride: [
              "heading",
              "bold",
              "italic",
              "code",
              "codeBlock",
              "quote",
              "ul",
              "ol",
              "link",
              "image",
              "table",
              "raw",
            ],
          },
        ],
      },
      {
        name: "apps",
        label: "App 矩陣",
        path: "content/apps",
        format: "md",
        ui: {
          allowedActions: {
            create: false,
            delete: false,
          },
        },
        fields: [
          {
            type: "string",
            name: "title",
            label: "標題",
            isTitle: true,
            required: true,
          },
          {
            type: "string",
            name: "layout",
            label: "Layout",
            ui: { component: null },
          },
          {
            type: "string",
            name: "url",
            label: "URL",
            ui: { component: null },
          },
          {
            type: "string",
            name: "summary",
            label: "摘要",
          },
          {
            type: "rich-text",
            name: "body",
            label: "內文",
            isBody: true,
            toolbarOverride: [
              "heading",
              "bold",
              "italic",
              "quote",
              "ul",
              "ol",
              "link",
              "image",
              "table",
              "raw",
            ],
          },
        ],
      },
      {
        name: "about",
        label: "關於",
        path: "content",
        format: "md",
        ui: {
          allowedActions: {
            create: false,
            delete: false,
          },
        },
        match: {
          include: "about",
        },
        fields: [
          {
            type: "string",
            name: "title",
            label: "標題",
            isTitle: true,
            required: true,
          },
          {
            type: "string",
            name: "layout",
            label: "Layout",
            ui: { component: null },
          },
          {
            type: "string",
            name: "url",
            label: "URL",
            ui: { component: null },
          },
          {
            type: "string",
            name: "summary",
            label: "摘要",
          },
          {
            type: "rich-text",
            name: "body",
            label: "內文",
            isBody: true,
            toolbarOverride: [
              "heading",
              "bold",
              "italic",
              "quote",
              "ul",
              "ol",
              "link",
              "image",
              "table",
              "raw",
            ],
          },
        ],
      },
    ],
  },
});

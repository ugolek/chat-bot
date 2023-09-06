# Layout

::: callout 👉

### Header

This component is used to render the header section of the layout.

HeaderProps:

- `children?: React.ReactNode`: The children elements to be rendered inside the header.
- `avatarHandler?: () => void`: A function to handle the avatar click event.

### Footer

This component is used to render the footer section of the layout.

FooterProps:

- `initialProps: { termsUrl: string; policyUrl: string; }`: The initial props for the footer component.

### BaseLayout

This component is the base layout component that wraps the entire application.

BaseLayoutProps:

- `initialProps: any`: The initial props for the base layout component.
- `children: React.ReactNode`: The children elements to be rendered inside the layout.
- `withoutLayout?: boolean`: A flag to indicate whether to render the layout or not.
- `breadcrumbs?: any[]`: An array of breadcrumb items.

### HeaderBanner

This component is used to render a banner in the header section.

BannerProps:

- `id: number`: The ID of the banner.
- `active: boolean`: A flag to indicate whether the banner is active or not.
- `link: string`: The link URL for the banner.
- `link_text: string`: The text for the banner link.
- `text: string`: The text content of the banner.

### Loader

This component is used to render a loading spinner.

No props are required for this component.

:::
import React from 'react';
import { 
  Navbar, 
  NavbarBrand, 
  NavbarContent, 
  NavbarItem, 
  NavbarMenu,
  NavbarMenuItem,
  NavbarMenuToggle,
  Button,
  Link,
} from "@nextui-org/react";
import { GithubLogo, BookOpen } from "@phosphor-icons/react";
import Logo from '../assets/observerlogo-nb-blue.png'

const CustomNavbar = () => {
  const [isMenuOpen] = React.useState(false);

  const menuItems = [
    { name: "Features", href: "#features" },
    { name: "Components", href: "#components" },
    { name: "Documentation", href: "/docs" },
    { name: "Examples", href: "#examples" },
    { name: "GitHub", href: "https://github.com/your-repo/ObserverAI" },
  ];

  return (
    <Navbar 
      shouldHideOnScroll 
      maxWidth="xl" 
      className="bg-white/70 backdrop-blur-md border-b border-gray-200"
    >
<NavbarBrand>
  <div className="flex items-center">
    {/* Replace this div with your logo image */}
    <img 
      src={Logo} // Update this path to your logo's location
      alt="ObserverAI Logo"
      className="w-12 h-12" // Adjust size as needed
    />
    <p className="font-bold text-inherit text-xl bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
      ObserverAI
    </p>
  </div>
</NavbarBrand>

      {/* <NavbarContent className="hidden sm:flex gap-8" justify="center">
        <NavbarItem>
          <Link 
            href="#features" 
            className="text-gray-600 hover:text-gray-900 font-medium"
          >
            Features
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link 
            href="#components"
            className="text-gray-600 hover:text-gray-900 font-medium"
          >
            Components
          </Link>
        </NavbarItem>
        <NavbarItem>
          <Link 
            href="#examples"
            className="text-gray-600 hover:text-gray-900 font-medium"
          >
            Examples
          </Link>
        </NavbarItem>
      </NavbarContent> */}

      <NavbarContent justify="end">
        <NavbarItem className="hidden sm:flex">
          <Button 
            as={Link} 
            href="/docs"
            variant="bordered"
            className="text-gray-700 border-gray-300"
            startContent={<BookOpen className="w-4 h-4" />}
          >
            Docs
          </Button>
        </NavbarItem>
        <NavbarItem>
          <Button 
            as={Link}
            href="https://github.com/your-repo/ObserverAI"
            className="bg-gradient-to-r from-blue-600 to-purple-600 text-white font-medium"
            startContent={<GithubLogo className="w-4 h-4" />}
          >
            GitHub
          </Button>
        </NavbarItem>
      </NavbarContent>

      <NavbarMenuToggle
        aria-label={isMenuOpen ? "Close menu" : "Open menu"}
        className="sm:hidden"
      />

      <NavbarMenu className="bg-white/70 backdrop-blur-md pt-6">
        {menuItems.map((item, index) => (
          <NavbarMenuItem key={`${item.name}-${index}`}>
            <Link
              className="w-full text-gray-600 hover:text-gray-900 font-medium py-2"
              href={item.href}
              size="lg"
            >
              {item.name}
            </Link>
          </NavbarMenuItem>
        ))}
      </NavbarMenu>
    </Navbar>
  );
};

export default CustomNavbar;
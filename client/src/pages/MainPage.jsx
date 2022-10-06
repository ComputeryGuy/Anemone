import React, { useState } from "react";
import { ThemeProvider } from "styled-components";
import Layout from "../styles/Layout";
import { GlobalStyle } from "../styles/GlobalStyle";
import { lightTheme, darkTheme } from "../styles/theme";

export const ThemeContext = React.createContext(null);

const MainPage = () => {
  const [theme, setTheme] = useState('light');
  const themeStyle = theme === 'light' ? lightTheme : darkTheme;

  return (
    <ThemeContext.Provider value={{ setTheme, theme }}>
      <ThemeProvider theme={themeStyle}>
        <GlobalStyle />
        <>
          <Layout> 
          </Layout>
        </>
      </ThemeProvider>
    </ThemeContext.Provider>
  );
}

export default MainPage;
import React from "react";
import Sidebar from "./Sidebar";
import { SLayout, SMain } from "./Components";

const Layout = ({ children }) => {
    return (
        <SLayout>
            <Sidebar />
            <SMain>{children}</SMain>
        </SLayout>
    );
};

export default Layout;
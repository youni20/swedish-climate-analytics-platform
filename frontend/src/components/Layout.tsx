import React from 'react';
import { Link } from 'react-router-dom';

import { ThemeToggle } from './ThemeToggle';

const Layout = ({ children }: { children: React.ReactNode }) => {
    return (
        <div className="min-h-screen bg-background font-sans antialiased text-foreground">
            <nav className="border-b bg-card text-card-foreground">
                <div className="container mx-auto flex h-16 items-center px-4 justify-between">
                    <div className="flex items-center">
                        <div className="font-bold text-xl mr-8">Swedish Climate Analytics</div>
                        <div className="flex gap-6">
                            <Link to="/" className="text-sm font-medium hover:text-primary">Dashboard</Link>
                            <Link to="/analytics" className="text-sm font-medium hover:text-primary">Analytics</Link>
                        </div>
                    </div>
                    <ThemeToggle />
                </div>
            </nav>
            <main className="container mx-auto p-4 md:p-8">
                {children}
            </main>
        </div>
    );
};

export default Layout;

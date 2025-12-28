import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Analytics from './pages/Analytics';
import Dashboard from './pages/Dashboard';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Dashboard />} />
                <Route path="/analytics" element={<Analytics />} />
            </Routes>
        </Router>
    );
}

export default App;

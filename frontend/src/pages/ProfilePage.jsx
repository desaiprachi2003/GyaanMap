
// import { useState } from 'react';
// import { Edit3, Save, BarChart3, Download, Eye } from 'lucide-react';
// import { useNavigate } from 'react-router-dom';

// const ProfilePage = () => {
//   const navigate = useNavigate();    
//   const [isEditing, setIsEditing] = useState(false);
//   const [userData, setUserData] = useState({
//     fullName: 'Alex Johnson',
//     university: 'State University',
//     graduationYear: '2025',
//     email: 'alex.johnson@email.com',
//     major: 'Computer Science'
//   });

//   const [tempData, setTempData] = useState({ ...userData });

//   const handleEdit = () => {
//     setTempData({ ...userData });
//     setIsEditing(true);
//   };

//   const handleSave = () => {
//     setUserData({ ...tempData });
//     setIsEditing(false);
//   };

//   const handleChange = (field, value) => {
//     setTempData(prev => ({ ...prev, [field]: value }));
//   };

//   return (
//     <div className="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
//       <div className="max-w-7xl mx-auto">
//         {/* Main Page Title */}
//         <h1 className="text-3xl font-extrabold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
//           My Profile
//         </h1>
//         <p className="text-gray-600 mb-8">
//           Manage your account and view your career exploration journey
//         </p>

//         <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
//           {/* Left Column - Personal Information */}
//           <div className="lg:col-span-2 space-y-8">
//             {/* Personal Information Card */}
//             <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
//               <div className="flex justify-between items-center mb-6">
//                 <h2 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
//                   Personal Information
//                 </h2>
//                 {isEditing ? (
//                   <button
//                     onClick={handleSave}
//                     className="flex items-center text-green-600 hover:text-green-700 font-medium"
//                   >
//                     <Save size={18} className="mr-1" />
//                     Save Changes
//                   </button>
//                 ) : (
//                   <button
//                     onClick={handleEdit}
//                     className="flex items-center text-blue-600 hover:text-blue-700 font-medium"
//                   >
//                     <Edit3 size={18} className="mr-1" />
//                     Edit
//                   </button>
//                 )}
//               </div>

//               <div className="space-y-4">
//                 {/* Input Fields */}
//                 <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Full Name
//                     </label>
//                     {isEditing ? (
//                       <input
//                         type="text"
//                         value={tempData.fullName}
//                         onChange={(e) => handleChange('fullName', e.target.value)}
//                         className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
//                       />
//                     ) : (
//                       <p className="text-gray-900">{userData.fullName}</p>
//                     )}
//                   </div>

//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       University
//                     </label>
//                     {isEditing ? (
//                       <input
//                         type="text"
//                         value={tempData.university}
//                         onChange={(e) => handleChange('university', e.target.value)}
//                         className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
//                       />
//                     ) : (
//                       <p className="text-gray-900">{userData.university}</p>
//                     )}
//                   </div>
//                 </div>

//                 <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Expected Graduation
//                     </label>
//                     {isEditing ? (
//                       <input
//                         type="text"
//                         value={tempData.graduationYear}
//                         onChange={(e) =>
//                           handleChange('graduationYear', e.target.value)
//                         }
//                         className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
//                       />
//                     ) : (
//                       <p className="text-gray-900">{userData.graduationYear}</p>
//                     )}
//                   </div>

//                   <div>
//                     <label className="block text-sm font-medium text-gray-700 mb-1">
//                       Major
//                     </label>
//                     {isEditing ? (
//                       <input
//                         type="text"
//                         value={tempData.major}
//                         onChange={(e) => handleChange('major', e.target.value)}
//                         className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
//                       />
//                     ) : (
//                       <p className="text-gray-900">{userData.major}</p>
//                     )}
//                   </div>
//                 </div>

//                 <div>
//                   <label className="block text-sm font-medium text-gray-700 mb-1">
//                     Email
//                   </label>
//                   {isEditing ? (
//                     <input
//                       type="email"
//                       value={tempData.email}
//                       onChange={(e) => handleChange('email', e.target.value)}
//                       className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
//                     />
//                   ) : (
//                     <p className="text-gray-900">{userData.email}</p>
//                   )}
//                 </div>
//               </div>
//             </div>

//             {/* Recent Activity Card */}
//             <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
//               <h2 className="text-xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
//                 Recent Activity
//               </h2>

//               <div className="space-y-4">
//                 <div className="flex items-start">
//                   <div className="bg-blue-100 p-2 rounded-full mr-4">
//                     <BarChart3 size={20} className="text-blue-600" />
//                   </div>
//                   <div>
//                     <p className="text-gray-900">Completed Career Quiz</p>
//                     <p className="text-gray-500 text-sm">2 days ago</p>
//                   </div>
//                 </div>

//                 <div className="flex items-start">
//                   <div className="bg-green-100 p-2 rounded-full mr-4">
//                     <Save size={20} className="text-green-600" />
//                   </div>
//                   <div>
//                     <p className="text-gray-900">Saved Software Engineer path</p>
//                     <p className="text-gray-500 text-sm">3 days ago</p>
//                   </div>
//                 </div>

//                 <div className="flex items-start">
//                   <div className="bg-purple-100 p-2 rounded-full mr-4">
//                     <Eye size={20} className="text-purple-600" />
//                   </div>
//                   <div>
//                     <p className="text-gray-900">Viewed UX Designer roadmap</p>
//                     <p className="text-gray-500 text-sm">1 week ago</p>
//                   </div>
//                 </div>

//                 <div className="flex items-start">
//                   <div className="bg-amber-100 p-2 rounded-full mr-4">
//                     <Download size={20} className="text-amber-600" />
//                   </div>
//                   <div>
//                     <p className="text-gray-900">Downloaded resources guide</p>
//                     <p className="text-gray-500 text-sm">1 week ago</p>
//                   </div>
//                 </div>
//               </div>
//             </div>
//           </div>

//           {/* Right Column - Stats and Info */}
//           <div className="space-y-8">
//             {/* Your Journey Card */}
//             <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
//               <h2 className="text-xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
//                 Your Journey
//               </h2>

//               <div className="grid grid-cols-2 gap-4">
//                 <div className="bg-blue-50 rounded-lg p-4 text-center">
//                   <p className="text-2xl font-bold text-blue-700">5</p>
//                   <p className="text-sm text-gray-600">Quizzes Taken</p>
//                 </div>

//                 <div className="bg-green-50 rounded-lg p-4 text-center">
//                   <p className="text-2xl font-bold text-green-700">12</p>
//                   <p className="text-sm text-gray-600">Careers Explored</p>
//                 </div>
//               </div>
//             </div>

//             {/* Member Since Card */}
//             <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
//               <h2 className="text-xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
//                 Member Since
//               </h2>
//               <p className="text-lg text-gray-900">January 2024</p>
//             </div>

//             {/* Quick Actions Card */}
//             <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
//               <h2 className="text-xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
//                 Quick Actions
//               </h2>

//               <div className="space-y-3">
//                 {/* <button className="w-full flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gradient-to-r from-purple-500 to-pink-500 hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500">
//                   Take New Quiz
//                 </button> */}

//                 <button
//                   onClick={() => navigate("/quiz")} // ✅ Redirect to /quiz
//                   className="w-full flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gradient-to-r from-purple-500 to-pink-500 hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
//                 >
//                   Take New Quiz
//                 </button>

             
//               </div>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// };

// export default ProfilePage;
//******************************************************************************************************************* */
import { useState, useEffect } from "react";
import { Edit3, Save, BarChart3, Download, Eye } from "lucide-react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const ProfilePage = () => {
  const navigate = useNavigate();
  const [isEditing, setIsEditing] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const [userData, setUserData] = useState({
    fullName: "",
    university: "",
    graduationYear: "",
    email: "",
    major: "",
  });

  const [tempData, setTempData] = useState({ ...userData });

  // Fetch profile on mount
  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const token = localStorage.getItem("token");
        if (!token) {
          navigate("/login");
          return;
        }

        axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;

        const res = await axios.get("http://localhost:5000/api/profile/me");
        const backend = res.data;

        setUserData({
          fullName: backend.name || "",
          university: backend.university || "",
          graduationYear: backend.graduationYear
            ? String(backend.graduationYear)
            : "",
          email: backend.email || "",
          major: backend.major || "",
        });

        setTempData({
          fullName: backend.name || "",
          university: backend.university || "",
          graduationYear: backend.graduationYear
            ? String(backend.graduationYear)
            : "",
          email: backend.email || "",
          major: backend.major || "",
        });
      } catch (err) {
        console.error("Fetch profile error:", err);
        if (err.response?.status === 401) {
          localStorage.removeItem("token");
          navigate("/login");
        } else {
          setError("Failed to load profile. Please try again.");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, [navigate]);

  // Handle save (update profile)
  const handleSave = async () => {
    try {
      const token = localStorage.getItem("token");
      axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;

      const payload = {
        name: tempData.fullName,
        university: tempData.university,
        graduationYear: tempData.graduationYear,
        major: tempData.major,
      };

      const res = await axios.put("http://localhost:5000/api/profile/me", payload);
      const updated = res.data;

      setUserData({
        fullName: updated.name,
        university: updated.university,
        graduationYear: updated.graduationYear
          ? String(updated.graduationYear)
          : "",
        email: updated.email,
        major: updated.major,
      });

      setIsEditing(false);
    } catch (err) {
      console.error("Update profile error:", err);
      setError("Failed to update profile. Please try again.");
    }
  };

  const handleEdit = () => {
    setTempData({ ...userData });
    setIsEditing(true);
  };

  const handleChange = (field, value) => {
    setTempData((prev) => ({ ...prev, [field]: value }));
  };

  if (loading) return <div className="p-10 text-center text-gray-600">Loading profile...</div>;
  if (error) return <div className="p-10 text-center text-red-600">{error}</div>;

  return (
    <div className="min-h-screen bg-gray-50 py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto">
        {/* Main Page Title */}
        <h1 className="text-3xl font-extrabold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
          My Profile
        </h1>
        <p className="text-gray-600 mb-8">
          Manage your account and view your career exploration journey
        </p>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Left Column - Personal Information */}
          <div className="lg:col-span-2 space-y-8">
            {/* Personal Information Card */}
            <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
              <div className="flex justify-between items-center mb-6">
                <h2 className="text-xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
                  Personal Information
                </h2>
                {isEditing ? (
                  <button
                    onClick={handleSave}
                    className="flex items-center text-green-600 hover:text-green-700 font-medium"
                  >
                    <Save size={18} className="mr-1" />
                    Save Changes
                  </button>
                ) : (
                  <button
                    onClick={handleEdit}
                    className="flex items-center text-blue-600 hover:text-blue-700 font-medium"
                  >
                    <Edit3 size={18} className="mr-1" />
                    Edit
                  </button>
                )}
              </div>

              <div className="space-y-4">
                {/* Input Fields */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Full Name
                    </label>
                    {isEditing ? (
                      <input
                        type="text"
                        value={tempData.fullName}
                        onChange={(e) => handleChange("fullName", e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      />
                    ) : (
                      <p className="text-gray-900">{userData.fullName}</p>
                    )}
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      University
                    </label>
                    {isEditing ? (
                      <input
                        type="text"
                        value={tempData.university}
                        onChange={(e) => handleChange("university", e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      />
                    ) : (
                      <p className="text-gray-900">{userData.university}</p>
                    )}
                  </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Expected Graduation
                    </label>
                    {isEditing ? (
                      <input
                        type="text"
                        value={tempData.graduationYear}
                        onChange={(e) => handleChange("graduationYear", e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      />
                    ) : (
                      <p className="text-gray-900">{userData.graduationYear}</p>
                    )}
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      Major
                    </label>
                    {isEditing ? (
                      <input
                        type="text"
                        value={tempData.major}
                        onChange={(e) => handleChange("major", e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
                      />
                    ) : (
                      <p className="text-gray-900">{userData.major}</p>
                    )}
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Email
                  </label>
                  <p className="text-gray-900">{userData.email}</p>
                </div>
              </div>
            </div>

            {/* Recent Activity Card */}
            <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
              <h2 className="text-xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
                Recent Activity
              </h2>

              <div className="space-y-4">
                <div className="flex items-start">
                  <div className="bg-blue-100 p-2 rounded-full mr-4">
                    <BarChart3 size={20} className="text-blue-600" />
                  </div>
                  <div>
                    <p className="text-gray-900">Completed Career Quiz</p>
                    <p className="text-gray-500 text-sm">2 days ago</p>
                  </div>
                </div>

                <div className="flex items-start">
                  <div className="bg-green-100 p-2 rounded-full mr-4">
                    <Save size={20} className="text-green-600" />
                  </div>
                  <div>
                    <p className="text-gray-900">Saved Software Engineer path</p>
                    <p className="text-gray-500 text-sm">3 days ago</p>
                  </div>
                </div>

                <div className="flex items-start">
                  <div className="bg-purple-100 p-2 rounded-full mr-4">
                    <Eye size={20} className="text-purple-600" />
                  </div>
                  <div>
                    <p className="text-gray-900">Viewed UX Designer roadmap</p>
                    <p className="text-gray-500 text-sm">1 week ago</p>
                  </div>
                </div>

                <div className="flex items-start">
                  <div className="bg-amber-100 p-2 rounded-full mr-4">
                    <Download size={20} className="text-amber-600" />
                  </div>
                  <div>
                    <p className="text-gray-900">Downloaded resources guide</p>
                    <p className="text-gray-500 text-sm">1 week ago</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Right Column - Stats and Info */}
          <div className="space-y-8">
            {/* Your Journey Card */}
            <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
              <h2 className="text-xl font-bold mb-6 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
                Your Journey
              </h2>

              <div className="grid grid-cols-2 gap-4">
                <div className="bg-blue-50 rounded-lg p-4 text-center">
                  <p className="text-2xl font-bold text-blue-700">5</p>
                  <p className="text-sm text-gray-600">Quizzes Taken</p>
                </div>

                <div className="bg-green-50 rounded-lg p-4 text-center">
                  <p className="text-2xl font-bold text-green-700">12</p>
                  <p className="text-sm text-gray-600">Careers Explored</p>
                </div>
              </div>
            </div>

            {/* Member Since Card */}
            <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
              <h2 className="text-xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
                Member Since
              </h2>
              <p className="text-lg text-gray-900">January 2024</p>
            </div>

            {/* Quick Actions Card */}
            <div className="bg-white rounded-xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-[0_6px_20px_rgba(168,85,247,0.4)]">
              <h2 className="text-xl font-bold mb-4 bg-clip-text text-transparent bg-gradient-to-r from-blue-500 to-indigo-600">
                Quick Actions
              </h2>

              <div className="space-y-3">
                <button
                  onClick={() => navigate("/quiz")}
                  className="w-full flex items-center justify-center px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-gradient-to-r from-purple-500 to-pink-500 hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500"
                >
                  Take New Quiz
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProfilePage;

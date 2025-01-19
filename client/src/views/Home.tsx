import { Button, Card } from "@nextui-org/react";
import {
  GithubLogo,
  BookOpen,
  Code,
  Database,
  Brain,
  Gauge,
  Robot,
  Lightning,
  Cpu,
  GitBranch,
  Terminal,
  Rocket,
  Stool,
  Star,
  Users,
  Graph,
  ArrowRight,
  CheckCircle,
  Shield,
  Gear,
} from "@phosphor-icons/react";
import Logo from '../assets/observerlogo-nb-blue.png'

// Keeping your existing FloatingOrb component
const FloatingOrb = ({ delay, duration, size, color, left, top }) => (
  <div
    className={`absolute rounded-full blur-xl animate-float ${size} ${color}`}
    style={{
      left,
      top,
      animation: `float ${duration}s infinite ease-in-out`,
      animationDelay: `${delay}s`,
    }}
  />
);

const LandingPage = () => {
  return (
    <div className="bg-gradient-to-b from-white to-gray-50">
      {/* Hero Section - Updated with brighter colors */}
      <div className="relative min-h-screen overflow-hidden bg-gradient-to-br from-blue-50 via-purple-50 to-white">
        <div className="absolute inset-0 bg-grid-blue-500/[0.02]" />

        <FloatingOrb
          delay={0}
          duration={8}
          size="w-64 h-64"
          color="bg-blue-400/20"
          left="10%"
          top="20%"
        />
        <FloatingOrb
          delay={1}
          duration={10}
          size="w-96 h-96"
          color="bg-purple-400/20"
          left="60%"
          top="10%"
        />
        <FloatingOrb
          delay={2}
          duration={9}
          size="w-72 h-72"
          color="bg-cyan-400/20"
          left="30%"
          top="60%"
        />

        <div className="relative z-10 flex min-h-screen justify-center items-center px-4">
          <div className="max-w-6xl mx-auto text-center">
            <div className="space-y-12">
              <div className="flex flex-col items-center gap-6 animate-fade-in">
                <div className="relative">
                  {/* <img
                    src={Logo}
                    alt="ObserverAI Logo"
                    className="w-50 h-40"
                  /> */}
                  <div className="absolute -inset-4 bg-blue-500/10 rounded-full blur-xl -z-10" />
                </div>
                <h1 className="text-4xl md:text-6xl lg:text-7xl font-bold">
                  <span className="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 via-purple-600 to-cyan-600">
                    ObserverAI
                  </span>
                </h1>
                <h2 className="text-3xl md:text-4xl lg:text-5xl text-gray-800 font-medium mt-4">
                  Track AI Decision Paths
                </h2>
              </div>

              <p className="text-lg md:text-xl text-gray-600 max-w-2xl mx-auto animate-fade-in-delayed">
                Advanced framework for tracking and analyzing AI agent decision
                paths. Understand, evaluate, and enhance your AI's
                decision-making process.
              </p>

              <div className="flex flex-col sm:flex-row gap-4 justify-center items-center animate-fade-in-delayed">
                <Button
                  href="https://github.com/your-repo/ObserverAI"
                  size="lg"
                  className="bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-lg hover:shadow-xl transform hover:-translate-y-0.5 transition-all"
                  startContent={
                    <GithubLogo weight="bold" className="w-5 h-5" />
                  }
                >
                  View on GitHub
                </Button>
                <Button
                  href="/docs"
                  size="lg"
                  variant="bordered"
                  className="border-purple-500 text-purple-600 hover:bg-purple-50"
                  startContent={<BookOpen weight="bold" className="w-5 h-5" />}
                >
                  Documentation
                </Button>
              </div>

              {/* Quick Stats */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-12 max-w-3xl mx-auto">
                {[
                  {
                    number: "99.9%",
                    label: "Accuracy",
                    icon: <CheckCircle className="w-5 h-5 text-green-500" />,
                  },
                  {
                    number: "50ms",
                    label: "Response Time",
                    icon: <Lightning className="w-5 h-5 text-yellow-500" />,
                  },
                  {
                    number: "10K+",
                    label: "Decision Paths",
                    icon: <GitBranch className="w-5 h-5 text-blue-500" />,
                  },
                  {
                    number: "24/7",
                    label: "Monitoring",
                    icon: <Gauge className="w-5 h-5 text-purple-500" />,
                  },
                ].map((stat, index) => (
                  <Card
                    key={index}
                    className="p-4 bg-white/80 backdrop-blur shadow-md hover:shadow-lg transition-all"
                  >
                    <div className="flex items-center gap-2 mb-2">
                      {stat.icon}
                    </div>
                    <p className="text-2xl font-bold text-gray-800">
                      {stat.number}
                    </p>
                    <p className="text-sm text-gray-600">{stat.label}</p>
                  </Card>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Curved separator */}
        <div className="absolute bottom-0 left-0 right-0">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 1440 320"
            className="w-full h-auto"
          >
            <path
              fill="#ffffff"
              fillOpacity="1"
              d="M0,96L48,112C96,128,192,160,288,160C384,160,480,128,576,122.7C672,117,768,139,864,144C960,149,1056,139,1152,122.7C1248,107,1344,85,1392,74.7L1440,64L1440,320L1392,320C1344,320,1248,320,1152,320C1056,320,960,320,864,320C768,320,672,320,576,320C480,320,384,320,288,320C192,320,96,320,48,320L0,320Z"
            ></path>
          </svg>
        </div>
      </div>

      {/* Why ObserverAI Section */}
      <section className="py-24 bg-white relative overflow-hidden">
        <div className="absolute inset-0 bg-grid-gray-500/[0.02]" />
        <div className="max-w-7xl mx-auto px-4 relative">
          <div className="text-center mb-16">
            <span className="text-blue-600 font-semibold text-sm uppercase tracking-wider">
              Why Choose ObserverAI
            </span>
            <h2 className="text-4xl font-bold text-gray-900 mt-2 mb-4">
              Powerful AI Decision Tracking
            </h2>
            <p className="text-gray-600 text-lg max-w-2xl mx-auto">
              Transform your AI development workflow with comprehensive decision
              tracking and analysis
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {[
              {
                icon: (
                  <Brain weight="duotone" className="w-12 h-12 text-blue-500" />
                ),
                title: "Intelligent Analysis",
                description:
                  "Advanced algorithms analyze decision patterns and provide actionable insights for improvement",
                features: [
                  "Pattern Recognition",
                  "Anomaly Detection",
                  "Performance Metrics",
                ],
              },
              {
                icon: (
                  <Shield
                    weight="duotone"
                    className="w-12 h-12 text-purple-500"
                  />
                ),
                title: "Robust & Reliable",
                description:
                  "Built with reliability in mind, ensuring your AI monitoring never misses a beat",
                features: ["99.9% Uptime", "Data Integrity", "Secure Storage"],
              },
              {
                icon: (
                  <Gear weight="duotone" className="w-12 h-12 text-cyan-500" />
                ),
                title: "Seamless Integration",
                description:
                  "Easily integrate with your existing AI infrastructure and start tracking immediately",
                features: ["Quick Setup", "API Support", "Multiple Frameworks"],
              },
            ].map((feature, index) => (
              <Card
                key={index}
                className="bg-white border-2 border-gray-100 hover:border-blue-100 transition-all p-6"
              >
                <div className="mb-4">{feature.icon}</div>
                <h3 className="text-xl font-semibold text-gray-900 mb-3">
                  {feature.title}
                </h3>
                <p className="text-gray-600 mb-4">{feature.description}</p>
                <ul className="space-y-2">
                  {feature.features.map((item, i) => (
                    <li
                      key={i}
                      className="flex items-center gap-2 text-gray-700"
                    >
                      <CheckCircle
                        weight="fill"
                        className="w-4 h-4 text-green-500"
                      />
                      {item}
                    </li>
                  ))}
                </ul>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Core Components Section */}
      <section className="py-24 bg-gradient-to-b from-gray-50 to-white relative overflow-hidden">
        <div className="absolute inset-0 bg-grid-gray-500/[0.02]" />
        <FloatingOrb
          delay={1}
          duration={12}
          size="w-96 h-96"
          color="bg-blue-400/10"
          left="-10%"
          top="20%"
        />
        <FloatingOrb
          delay={2}
          duration={15}
          size="w-96 h-96"
          color="bg-purple-400/10"
          left="80%"
          top="60%"
        />

        <div className="max-w-7xl mx-auto px-4 relative">
          <div className="text-center mb-16">
            <span className="text-purple-600 font-semibold text-sm uppercase tracking-wider">
              Core Components
            </span>
            <h2 className="text-4xl font-bold text-gray-900 mt-2 mb-4">
              Built for Scale
            </h2>
            <p className="text-gray-600 text-lg max-w-2xl mx-auto">
              Powerful tools designed to handle complex AI decision tracking at
              any scale
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {[
              {
                icon: <Brain weight="duotone" className="w-16 h-16" />,
                title: "Observer",
                description:
                  "Manages observation sessions, ensuring systematic decision tracking",
                features: [
                  "Real-time Monitoring",
                  "Custom Events",
                  "Data Export",
                ],
              },
              {
                icon: <GitBranch weight="duotone" className="w-16 h-16" />,
                title: "Decision Path",
                description:
                  "Encapsulates steps, context, and reasoning behind agent decisions",
                features: [
                  "Path Visualization",
                  "Context Tracking",
                  "Reasoning Analysis",
                ],
              },
              {
                icon: <Robot weight="duotone" className="w-16 h-16" />,
                title: "Enhanced Agent",
                description:
                  "Structured methods for complex tasks with detailed analytics",
                features: [
                  "Advanced Analytics",
                  "Task Management",
                  "Performance Tracking",
                ],
              },
              {
                icon: <Cpu weight="duotone" className="w-16 h-16" />,
                title: "SWARM Adapter",
                description:
                  "Standardized format conversion for SWARM agent outputs",
                features: [
                  "Format Conversion",
                  "Data Normalization",
                  "Batch Processing",
                ],
              },
            ].map((component, index) => (
              <Card
                key={index}
                className="bg-white p-6 hover:shadow-lg transition-all border-2 border-gray-100"
              >
                <div className="text-purple-500 mb-4">{component.icon}</div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  {component.title}
                </h3>
                <p className="text-gray-600 mb-4">{component.description}</p>
                <ul className="space-y-2">
                  {component.features.map((feature, i) => (
                    <li
                      key={i}
                      className="flex items-center gap-2 text-gray-700 text-sm"
                    >
                      <ArrowRight
                        weight="bold"
                        className="w-4 h-4 text-purple-500"
                      />
                      {feature}
                    </li>
                  ))}
                </ul>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Installation Section */}
      <section className="py-24 bg-gradient-to-br from-purple-50 via-white to-blue-50 relative overflow-hidden">
        <div className="absolute inset-0 bg-grid-gray-500/[0.02]" />
        <div className="max-w-7xl mx-auto px-4 relative">
          <div className="text-center mb-16">
            <span className="text-blue-600 font-semibold text-sm uppercase tracking-wider">
              Get Started
            </span>
            <h2 className="text-4xl font-bold text-gray-900 mt-2 mb-4">
              Quick Installation
            </h2>
            <p className="text-gray-600 text-lg max-w-2xl mx-auto">
              Get up and running with ObserverAI in minutes
            </p>
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <div className="space-y-8">
              <Card className="bg-white border-2 border-gray-100">
                <div className="p-6">
                  <div className="flex items-center gap-2 text-gray-700 mb-4">
                    <Terminal
                      weight="bold"
                      className="w-5 h-5 text-purple-500"
                    />
                    <span className="font-medium">Simple Installation</span>
                  </div>
                  <div className="bg-gray-900 rounded-lg p-4 font-mono text-sm">
                    <p className="text-gray-400"># Clone the repository</p>
                    <p className="text-purple-400">
                      git clone https://github.com/your-repo/ObserverAI.git
                    </p>
                    <p className="text-gray-400 mt-2"># Navigate to project</p>
                    <p className="text-purple-400">cd ObserverAI</p>
                    <p className="text-gray-400 mt-2"># Install dependencies</p>
                    // Previous code remains the same until installation section
                    continuation...
                    <p className="text-purple-400">poetry install</p>
                  </div>
                </div>
              </Card>

              <div className="space-y-6">
                <div className="bg-white p-6 rounded-xl border-2 border-gray-100 hover:border-blue-100 transition-all">
                  <div className="flex items-center gap-3 mb-2">
                    <Lightning
                      weight="duotone"
                      className="w-8 h-8 text-yellow-500"
                    />
                    <h3 className="text-xl font-semibold text-gray-900">
                      Lightning Fast Setup
                    </h3>
                  </div>
                  <p className="text-gray-600 ml-11">
                    Get started in minutes with our streamlined installation
                    process
                  </p>
                </div>

                <div className="bg-white p-6 rounded-xl border-2 border-gray-100 hover:border-blue-100 transition-all">
                  <div className="flex items-center gap-3 mb-2">
                    <Database
                      weight="duotone"
                      className="w-8 h-8 text-blue-500"
                    />
                    <h3 className="text-xl font-semibold text-gray-900">
                      Simple Configuration
                    </h3>
                  </div>
                  <p className="text-gray-600 ml-11">
                    Easy environment setup with comprehensive documentation
                  </p>
                </div>

                <div className="bg-white p-6 rounded-xl border-2 border-gray-100 hover:border-blue-100 transition-all">
                  <div className="flex items-center gap-3 mb-2">
                    <Rocket
                      weight="duotone"
                      className="w-8 h-8 text-purple-500"
                    />
                    <h3 className="text-xl font-semibold text-gray-900">
                      Ready to Scale
                    </h3>
                  </div>
                  <p className="text-gray-600 ml-11">
                    Built to handle enterprise-level AI decision tracking needs
                  </p>
                </div>
              </div>
            </div>

            {/* Configuration Example */}
            <div className="space-y-6">
              <Card className="bg-white border-2 border-gray-100">
                <div className="p-6">
                  <div className="flex items-center gap-2 text-gray-700 mb-4">
                    <Code weight="bold" className="w-5 h-5 text-blue-500" />
                    <span className="font-medium">Quick Configuration</span>
                  </div>
                  <div className="bg-gray-900 rounded-lg p-4 font-mono text-sm">
                    <p className="text-gray-400"># Example .env file</p>
                    <p className="text-blue-400">
                      DATABASE_URL=sqlite:///observerai.db
                    </p>
                    <p className="text-blue-400">API_KEY=your_api_key</p>
                    <p className="text-blue-400">DEBUG=True</p>
                    <p className="text-gray-400 mt-4"># Basic usage example</p>
                    <p className="text-purple-400">
                      from observerai.observer import Observer
                    </p>
                    <p className="text-purple-400">observer = Observer()</p>
                    <p className="text-purple-400">
                      with observer.session("Analysis") as session:
                    </p>
                    <p className="text-purple-400"> session.record(decision)</p>
                  </div>
                </div>
              </Card>
            </div>
          </div>
        </div>
      </section>

      {/* Use Cases Section */}
      <section className="py-24 bg-white relative overflow-hidden">
        <div className="absolute inset-0 bg-grid-gray-500/[0.02]" />
        <FloatingOrb
          delay={3}
          duration={10}
          size="w-96 h-96"
          color="bg-cyan-400/10"
          left="70%"
          top="20%"
        />

        <div className="max-w-7xl mx-auto px-4 relative">
          <div className="text-center mb-16">
            <span className="text-cyan-600 font-semibold text-sm uppercase tracking-wider">
              Use Cases
            </span>
            <h2 className="text-4xl font-bold text-gray-900 mt-2 mb-4">
              Endless Possibilities
            </h2>
            <p className="text-gray-600 text-lg max-w-2xl mx-auto">
              Discover how ObserverAI can transform your AI operations
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[
              {
                icon: (
                  <Graph weight="duotone" className="w-12 h-12 text-blue-500" />
                ),
                title: "Financial Analysis",
                description:
                  "Track AI trading decisions and market analysis patterns",
                benefits: [
                  "Risk Assessment",
                  "Pattern Recognition",
                  "Performance Tracking",
                ],
              },
              {
                icon: (
                  <Users
                    weight="duotone"
                    className="w-12 h-12 text-purple-500"
                  />
                ),
                title: "Customer Service",
                description: "Monitor AI support agent decisions and responses",
                benefits: [
                  "Response Quality",
                  "Customer Satisfaction",
                  "Agent Performance",
                ],
              },
              {
                icon: (
                  <Shield
                    weight="duotone"
                    className="w-12 h-12 text-cyan-500"
                  />
                ),
                title: "Security Operations",
                description:
                  "Analyze AI threat detection and response patterns",
                benefits: [
                  "Threat Detection",
                  "Response Time",
                  "Security Metrics",
                ],
              },
              {
                icon: (
                  <Stool
                    weight="duotone"
                    className="w-12 h-12 text-yellow-500"
                  />
                ),
                title: "DevOps & Testing",
                description:
                  "Track AI-powered testing and deployment decisions",
                benefits: [
                  "Quality Assurance",
                  "Deployment Success",
                  "Bug Prevention",
                ],
              },
              {
                icon: (
                  <Brain
                    weight="duotone"
                    className="w-12 h-12 text-green-500"
                  />
                ),
                title: "Research & Development",
                description: "Monitor AI experiment decisions and outcomes",
                benefits: [
                  "Experiment Tracking",
                  "Result Analysis",
                  "Innovation Metrics",
                ],
              },
              {
                icon: (
                  <Star weight="duotone" className="w-12 h-12 text-red-500" />
                ),
                title: "Product Recommendations",
                description: "Track AI recommendation engine decisions",
                benefits: [
                  "Accuracy Metrics",
                  "User Engagement",
                  "Sales Impact",
                ],
              },
            ].map((useCase, index) => (
              <Card
                key={index}
                className="bg-white border-2 border-gray-100 hover:border-blue-100 transition-all p-6"
              >
                <div className="mb-4">{useCase.icon}</div>
                <h3 className="text-xl font-semibold text-gray-900 mb-3">
                  {useCase.title}
                </h3>
                <p className="text-gray-600 mb-4">{useCase.description}</p>
                <ul className="space-y-2">
                  {useCase.benefits.map((benefit, i) => (
                    <li
                      key={i}
                      className="flex items-center gap-2 text-gray-700"
                    >
                      <CheckCircle
                        weight="fill"
                        className="w-4 h-4 text-green-500"
                      />
                      {benefit}
                    </li>
                  ))}
                </ul>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Your existing styles remain the same */}
      <style jsx>{`
        @keyframes float {
          0%,
          100% {
            transform: translate(0, 0);
            opacity: 0.4;
          }
          50% {
            transform: translate(10px, -20px);
            opacity: 0.8;
          }
        }
        @keyframes fade-in {
          from {
            opacity: 0;
            transform: translateY(-20px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-float {
          animation: float 8s infinite ease-in-out;
        }
        .animate-fade-in {
          animation: fade-in 1s ease-out forwards;
        }
        .animate-fade-in-delayed {
          animation: fade-in 1s ease-out 0.3s forwards;
          opacity: 0;
        }
      `}</style>
    </div>
  );
};

export default LandingPage;

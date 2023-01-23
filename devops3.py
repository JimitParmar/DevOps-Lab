pipeline {
    agent any

    stages {
        stage('Takenum') {
            steps {
               env.NUM = input value: 'Enter number',
                             parameters: [value(defaultValue: '',
                                          description: '',
                                          name: 'Number')]
            }
        }
        stage('runalgo') {
            steps {
                script {
                    if (env.NUM %2==0) {
                        echo 'Number is odd'
                    } else {
                        echo 'Number is even'
                    }
                }
            }
        }
    }
}

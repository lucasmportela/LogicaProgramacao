
            string nome;
            double med = 0;
            double prov1 = 0, prov2 = 0, sim = 0, pro = 0;
            int conf = 0;
            Console.WriteLine("Informe seu nome:");
            nome = Console.ReadLine();
            Console.Clear();

            Console.WriteLine("Olá " + nome + " informe sua nota");

            while (conf != 1)
            {
                Console.WriteLine("Primeira prova:"); 
                prov1 = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("Segunda prova:");
                prov2 = Convert.ToDouble(Console.ReadLine());

                if (prov1 >= 0 && prov1 <= 10 && prov2 >= 0 && prov2 <= 10)
                {
                    conf = 1;
                }
                else
                {
                    Console.WriteLine("Valor Inválido");
                    Console.ReadKey();
                    Console.Clear();
                }
            }
            Console.Clear();
            while (conf !=0)
            {
                Console.WriteLine("Simulado:");
                sim = Convert.ToDouble(Console.ReadLine());
                Console.WriteLine("Pontos extra:");
                pro = Convert.ToDouble(Console.ReadLine());

                if (sim >= 0 && sim <= 7 && pro >= 0 && pro <= 3)
                {
                    sim = sim + pro;
                    conf = 0;
                }
                else
                {
                    Console.WriteLine("Valor Inválido");
                    Console.ReadKey();
                    Console.Clear();
                }
            }

            med = (prov1 + prov2) / 2;
            med = (med + sim) / 2;
            Console.ReadKey();
            Console.Clear();
            if (med >=7)
            {
                Console.WriteLine("Parabéns " + nome + " você foi aprovado");
            }
            else if (med >=5)
            {
                Console.WriteLine(nome + " você está de recuperação");
            }
            else
            {
                Console.WriteLine(nome + " você foi reprovado");
            }
            Console.WriteLine("Sua média é: " + med.ToString("F2"));
            Console.ReadKey();

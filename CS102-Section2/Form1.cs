using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace CS102_Section2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                int grade = (int)Convert.ToInt64("90");

                if (grade>=90)
                {
                    MessageBox.Show("A");
                    this.Close();

                }
                else if(grade >= 80)
                {
                    MessageBox.Show("B");
                    this.Close();
                }
                else if (grade >= 70)
                {
                    MessageBox.Show("C");
                    this.Close();
                }
                else if (grade >= 60)
                {
                    MessageBox.Show("D");
                    this.Close();
                }
                else
                {
                    MessageBox.Show("F");
                    this.Close();
                }
               
            }
            catch (System.FormatException)
            {
                MessageBox.Show("Invalid Format");
                this.Close();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }

    }
}
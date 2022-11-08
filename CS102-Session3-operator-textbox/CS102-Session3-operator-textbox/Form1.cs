using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace CS102_Session3_operator_textbox
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }


        public void txt2_TextChanged(object sender, EventArgs e)
        {
            try
            {
                if (optxt.Text == "+")
                {
                   
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 + num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                    
                    
                }


                else if (optxt.Text == "-")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 - num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "x")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 * num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "*")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 * num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "/")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 / num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "%")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 % num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }
                
            }
            catch (System.FormatException)
            {
                label4.Text = "invalid input";
            }
        }

        public void txt1_TextChanged(object sender, EventArgs e)
        {
            try
            {
                if (optxt.Text == "+")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 + num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "-")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 - num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "x")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 * num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "*")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 * num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "/")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 / num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "%")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 % num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }
                
            }
            catch (System.FormatException)
            {
                label4.Text = "invalid input";
            }
        }

        private void optxt_TextChanged(object sender, EventArgs e)
        {
            try
            {
                if (optxt.Text == "+")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 + num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "-")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 - num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "x")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 * num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "*")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 * num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "/")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 / num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }


                else if (optxt.Text == "%")
                {
                    float num1 = float.Parse(txt1.Text);
                    float num2 = float.Parse(txt2.Text);
                    float sum = num1 % num2;
                    var sumstr = sum.ToString();
                    label4.Text = sumstr;
                }
                
            }
            catch (System.FormatException)
            {
                label4.Text = "invalid input";
            }
        
        }

        

        
    }
}